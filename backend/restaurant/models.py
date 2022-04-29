from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000, null=True, blank=True, default='')
    location = models.CharField(max_length=255, null=True, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.name

class City(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.CharField(max_length=5000, null=True, blank=True, default='')

    def __str__(self):
        return self.name

prices = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)

class Restaurant(models.Model):
    name = models.TextField(max_length=120)
    city = models.ForeignKey(to='City', on_delete=models.CASCADE, null=True, default=True, related_name='restaurant')
    image = models.CharField(max_length=1000, null=True, blank=True, default='')
    cuisine = models.CharField(max_length=255, null=True, blank=True, default='')
    price = models.CharField(max_length=1, choices=prices, null=True, blank=True, default='')
    created_on = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
