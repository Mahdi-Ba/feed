from abc import ABC, abstractmethod
from django.contrib.auth import authenticate

from rest_framework_jwt.settings import api_settings

from ..models import User


class UserService(ABC):
    def __init__(self):
        self.user = None

    @abstractmethod
    def check_user_authenticate(self):
        pass

    @abstractmethod
    def create_user(self):
        pass


class jWTMixin:
    def getToken(self, user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        return jwt_encode_handler(payload)


class JWTSimpleUserService(UserService, jWTMixin):
    def check_user_authenticate(self, username: str, password: str):
        self.user = authenticate(username=username, password=password)
        return self

    def create_user(self, username: str, password: str, kwargs: dict):
        self.user = User.objects.create_user(username, password, kwargs)
        return self

    def get_token(self) -> str:
        if self.user is None:
            raise Exception('user is None implement check_user_authenticate method')
        return self.getToken(self.user)
