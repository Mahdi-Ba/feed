from rest_framework.test import APITestCase

from .api.serializers import UserSerializer
from .models import User


class TestCase(APITestCase):
    def setUp(self):
        self.username = 'reza'
        self.password = '123456'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login(self, **kwargs):
        data = {
            "username": self.username,
            "password": self.password
        }
        res = self.client.post('/api/v1/users/login', data).json()
        assert res['success'] == True
        assert 'token' in res['data']
        assert res['data']['user_info'] == UserSerializer(self.user).data


    def test_register(self):
        data = {
            "username": self.username + '_test',
            "password": self.password
        }
        res = self.client.post('/api/v1/users/register', data).json()
        assert res['success'] == True
        assert 'token' in res['data']
