from django.db import models


# Create your models here.

# 微信信息主流水表
class MainTransLog(models.Model):
    FromUserName = models.CharField(max_length=100)
    CreateTime = models.CharField(max_length=30)
    MsgType = models.CharField(max_length=20)
    MsgId = models.CharField(max_length=70)
    TransTime = models.DateTimeField(auto_now_add=True)


# 空气质量-城市列表
class CityList(models.Model):
    CityName = models.CharField(max_length=10, primary_key=True)
    CityURL = models.CharField(max_length=50)


# 用户状态表
class UserList(models.Model):
    FromUserName = models.CharField(max_length=100, default='')
    UserStatus = models.CharField(max_length=3, default='00')


# 机器人对话流水表
class RobotLog(models.Model):
    FromUserName = models.CharField(max_length=100, default='')
    MsgId = models.CharField(max_length=70, default='')
    RobotType = models.CharField(max_length=2)  # 1-图灵 2-青云客 3-小i L-localAI
    TransTime = models.DateTimeField(auto_now_add=True)
    MsgType = models.CharField(max_length=20)
    ReqDict = models.CharField(max_length=2000)  # req_dict用字符串保存起来
    RspDict = models.CharField(max_length=2000)  # rsp_dict用字符串保存起来
