from django.utils.timezone import now
from rest_framework.test import APITestCase
from user.models import User
from .models import Channel, Article
from rest_framework import status


class TestCase(APITestCase):

    def setUp(self):
        self.token = None
        self.create_and_login()
        self.create_channel()
        self.create_article()

    def create_and_login(self):
        self.username = 'reza'
        self.password = '123456'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        data = {
            "username": self.username,
            "password": self.password
        }
        res = self.client.post('/api/v1/users/login', data).json()
        self.token = res['data']['token']
        self.client.credentials(HTTP_AUTHORIZATION='bearer ' + self.token)

    def create_channel(self):
        self.channel = Channel.objects.create(title='test', link='http://127.0.0.1', status=0, is_disable=False,
                                              description='test', publish_date=now(), last_build_date=now(),
                                              language='fa')

    def create_article(self):
        self.article = Article.objects.create(
            channel=self.channel, title='test', link='http://127.0.0.1', guid='9da0c990-e631-4988-8aa6-15e9714c44a4',
            author='ali', description='test', publish_date=now())

    def test_get_channel_info(self):
        res = self.client.get('/api/v1/rss/channel')
        assert res.json()['success'] == True
        assert 'data' in res.json()
        assert res.status_code == status.HTTP_200_OK

    def test_get_article_info(self):
        res = self.client.get(f'/api/v1/rss/channel/{self.channel.pk}/article')
        assert res.json()['success'] == True
        assert 'data' in res.json()
        assert res.status_code == status.HTTP_200_OK

    def test_toggle_follow_channel(self):
        data = {"id": self.channel.id}
        res = self.client.post('/api/v1/rss/channel/follow', data)
        assert res.json()['success'] == True
        assert self.user in self.channel.users.all()

        res = self.client.post('/api/v1/rss/channel/follow', data)
        assert res.json()['success'] == True
        assert self.user not in self.channel.users.all()

    def test_get_channel_follow(self):
        res = self.client.get('/api/v1/rss/channel/follow')
        assert res.json()['success'] == True
        assert 'data' in res.json()

    def test_get_article_favorite(self):
        res = self.client.get('/api/v1/rss/channel/article/favorite')
        assert res.json()['success'] == True
        assert 'data' in res.json()

    def test_toggle_article_channel(self):
        data = {"id": self.article.id}
        res = self.client.post('/api/v1/rss/channel/article/favorite', data)
        assert res.json()['success'] == True
        assert self.user in self.article.users.all()

        res = self.client.post('/api/v1/rss/channel/article/favorite', data)
        assert res.json()['success'] == True
        assert self.user not in self.article.users.all()







