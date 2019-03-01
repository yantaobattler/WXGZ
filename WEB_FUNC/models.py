from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=130)
    level = models.CharField(max_length=1)  # 0-管理员 1-普通用户
    last_login_time = models.DateTimeField()
    now_login_time = models.DateTimeField(auto_now_add=True)


class Suggest(models.Model):
    username = models.CharField(max_length=100)
    channel = models.CharField(max_length=10)   # wx001-围观实验室
    time = models.DateTimeField(auto_now_add=True)
    suggest = models.CharField(max_length=1000)
    dealflag = models.CharField(max_length=1, default='0')  # 0-未处理 1-已处理


class event(models.Model):
    username = models.CharField(max_length=1)