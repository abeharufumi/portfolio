from django.db import models
# from django.conf import settings
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
import os
# Create your models here.

# class AddModel(models.Model):
    # author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE) #モデル
    

class CustomUser(AbstractUser):
  # add = models.ForeignKey(AddModel, on_delete=models.PROTECT)
  memo = models.CharField(max_length=100)
  email = models.EmailField(verbose_name='Eメールアドレス',max_length=255,unique=True)
#   uploaded_at = models.DateTimeField(auto_now_add=True) #Trueならデータ作成時の日時が自動保存される
  statas = models.IntegerField(choices=[(1,"新規契約"),(2,"契約継続"),(3,"契約変更"),(4,"解約希望")]) #{{ get_statas_display }}
  # document = models.FileField(upload_to='document/', max_length=100)
  document = models.ImageField(upload_to='document/', max_length=100, null=True, blank=True)
  phoneNumber = models.CharField(max_length=11, unique=True, null=False, blank=False)
  # REQUIRED_FILEDS を設定することで、createsuperuser 実行時に username・email・password の入力受付が行われるようになり、上手くユーザーを作成することができるようになる。
  REQUIRED_FIELDS = ["email","statas"]
  def __str__(self):
      return self.username
  def file_name(self):
    return os.path.basename(self.document.name)


