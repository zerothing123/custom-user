from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,full_name,password=None,is_admin=False,is_active=True,is_staff=False):
        if not email:
            raise ValueError('users must have an email')
        if not password:
            raise ValueError('users must have a password')
        if not full_name:
            raise ValueError('users must have a fullname')
        user=self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )
        user.set_password(password)
        user.is_active=is_active
        user.is_admin=is_admin
        user.is_staff=is_staff
        user.save(using=self._db)
        return user
    def create_staffuser(self,email,full_name,password=None):
        user=self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        return user
    def create_superuser(self,email,full_name,password=None):
        user=self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user
class User(AbstractBaseUser):
    email=models.CharField(max_length=200,unique=True)
    full_name=models.CharField(max_length=200,blank=True,null=True)
    active=models.BooleanField(default=True)
    admin=models.BooleanField(default=False)
    staff=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['full_name']
    objects=UserManager()
    def __str__(self):
        return self.email
    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_lable):
        return True
    def is_admin(self):
        return self.admin
    def is_staff(self):
        return self.staff
    def is_active(self):
        return self.active