from django.utils.timezone import now
from rest_framework.test import APITestCase

from user.models import User

from .models import Channel, Article


class TestCase(APITestCase):
    def setUp(self):
        self.username = 'reza'
        self.password = '123456'
        User.objects.create_user(username=self.username, password=self.password)
        self.login()
        self.channel = Channel.objects.create(title='test', link='http://127.0.0.1', status=0, is_disable=False,
                                              description='test', publish_date=now(), last_build_date=now(),
                                              language='fa')
        self.article = Article.objects.create(
            channel=self.channel,title='test', link='http://127.0.0.1', guid='9da0c990-e631-4988-8aa6-15e9714c44a4',
            author='ali',description='test',publish_date=now())

    def login(self):
        data = {
            "username": self.username,
            "password": self.password
        }
        res = self.client.post('/api/v1/users/login', data).json()
        self.client.credentials(HTTP_AUTHORIZATION='bearer ' + res['data']['token'])

    def test_get_channel_info(self):
        res = self.client.get('/api/v1/rss/channel').json()
        print(res)
