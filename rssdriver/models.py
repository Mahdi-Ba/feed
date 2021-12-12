from django.db import models
from user.models import User
from django.utils.translation import gettext as _
import feedparser
import pytz
from datetime import datetime
from time import mktime


class Status(models.IntegerChoices):
    NOTHING = 0, _('NOTHING')
    MODIFY_SUPPORT = 1, _('MODIFY_SUPPORT')
    MODIFY_UN_SUPPORT = 2, _('MODIFY_UN_SUPPORT')


class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    channel = models.ForeignKey('Channel', null=True, on_delete=models.CASCADE)
    link = models.URLField()
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    guid = models.UUIDField(null=True, blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    users = models.ManyToManyField(User, blank=True)

    def toggle_favorite(self, user):
        if user.id in self.users.values_list('id', flat=True):
            self.users.remove(user)
        else:
            self.users.add(user)
            if user.id not in self.channel.users.values_list('id', flat=True):
                self.channel.users.add(user)


# https://www.irinn.ir/fa/rss/allnews
# https://lincolnproject.libsyn.com/rss
# https://feeds.fireside.fm/bibleinayear/rss
# https://rss.art19.com/apology-line
# https://feeds.fireside.fm/bibleinayear/rss
# https://feeds.megaphone.fm/ADL9840290619
class Channel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    link = models.URLField()
    status = models.IntegerField(choices=Status.choices, default=Status.NOTHING)
    is_disable = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    last_build_date = models.DateTimeField(blank=True, null=True)
    language = models.CharField(max_length=5, blank=True)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    def get_chanel_info(self):
        if self.status == Status.MODIFY_SUPPORT:
            self.feed_parser = feedparser.parse(self.link, modified=self.last_build_date)
        else:
            self.feed_parser = feedparser.parse(self.link)
            self.modify_checker()

        self.title = self.feed_parser.feed.title if 'title' in self.feed_parser.feed else self.title
        self.description = self.feed_parser.feed.description if 'description' in self.feed_parser.feed else self.description
        self.language = self.feed_parser.feed.language if 'language' in self.feed_parser.feed else ''
        self.save()
        return self

    @staticmethod
    def parsed_struct_time_to_datetime(struct_time):
        # tz = pytz.timezone('Asia/Tehran')
        # return datetime.fromtimestamp(mktime(struct_time), tz)
        return datetime.fromtimestamp(mktime(struct_time))

    def modify_checker(self):
        if 'modified' in self.feed_parser:
            self.status = Status.MODIFY_SUPPORT
            self.last_build_date = self.parsed_struct_time_to_datetime(self.feed_parser.modified_parsed)
            publish_date = self.feed_parser['items'][0].published_parsed
            self.publish_date = self.parsed_struct_time_to_datetime(publish_date)
        else:
            self.status = Status.MODIFY_UN_SUPPORT
            publish_date = self.feed_parser.feed.publish_date_parsed if 'publish_date' in self.feed_parser.feed else \
                self.feed_parser['items'][0]['published_parsed']
            self.publish_date = self.parsed_struct_time_to_datetime(publish_date)
        self.save()

    def create_article(self):
        # if self.last_build_date is not None and \
        #         int(self.last_build_date.strftime('%s')) == int(mktime(self.feed_parser.feed.updated_parsed)):
        #     self.feed_parser['items'].clear()
        # self.last_build_date = self.parsed_struct_time_to_datetime(self.feed_parser.feed.updated_parsed)
        # self.save()
        key_correct = ['title', 'channel', 'link', 'description', 'author', 'guid']
        article_list = []
        for article in self.feed_parser['items']:
            print(article)
            published_parsed = article.get('published_parsed')
            article_list.append(
                Article(channel=self, **{key: value for (key, value) in article.items() if key in key_correct},
                        publish_date=self.parsed_struct_time_to_datetime(published_parsed)
                        )
            )
        Article.objects.bulk_create(article_list)

    def toggle_Follow(self, user):
        if user.id in self.users.values_list('id', flat=True):
            self.users.remove(user)
        else:
            self.users.add(user)

# channel = Channel.objects.get(id=2)
# channel.get_chanel_info()
# channel.create_article()


#
# channel = Channel.objects.prefetch_related('users').first()
# channel.toggle_Follow(user=User.objects.first())
