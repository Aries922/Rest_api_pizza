from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using= self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser= True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Pizza_size(models.Model):
    size = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.size

class Pizza_topping(models.Model):
    topping = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.topping

class PizzaTypes(models.Model):

    TYPES = (
        ('Regular', 'regular'),
        ('Square', 'Square')
    )
    pizza_type = models.CharField(max_length=25,choices=TYPES)
    pizza_size = models.ManyToManyField(Pizza_size)
    pizza_toppings = models.ManyToManyField(Pizza_topping)
