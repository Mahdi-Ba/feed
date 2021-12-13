from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def _create_user(self, username, password=None, extra_fields=None):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, extra_fields=None):
        if isinstance(extra_fields,dict) :
            extra_fields._mutable = True
            extra_fields.pop('username', None)
            extra_fields.pop('password', None)
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, extra_fields)

    def create_superuser(self, username, password, email=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self._create_user(
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return self.username


