from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username, email, password = None):
        if not email:
            raise ValueError('enter email')
        user = self.model(  #ユーザークラスの呼び出し
            username = username,
            email = email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password = None):
        user = self.model(
            username=username,
            email = email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 255, unique = True)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)#管理画面にアクセスできるかどうか
    website = models.URLField(null = True)
    picture = models.FileField(null = True)
    USERNAME_FIELD = 'email'#ユーザーをこのテーブルで識別
    REQUIRED_FIELDS = ['username'] #スーパーユーザー作成時に入力

    objects = UserManager()

    def __str__(self):
        return self.email

