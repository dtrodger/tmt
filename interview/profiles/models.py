from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('last login'), default=timezone.now)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    is_admin = models.BooleanField(_('admin status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatars/', null=True, blank=True)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_username(self):
        return self.email

    # is_authenticated exists already on AbstractBaseUser
    # def is_authenticated(self):
    #     return True

    def __str__(self):
        return self.email