# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(verbose_name=u"昵称", max_length=30, default="")
    gender = models.CharField(verbose_name=u"性别", max_length=6, choices=(("male", u"男"), ("female", u"女")), default='female')
    mobile = models.CharField(verbose_name=u"手机号", max_length=11, null=True, blank=True)
    address = models.CharField(verbose_name=u"地址", max_length=100, default="")
    image = models.ImageField(verbose_name=u"头像", max_length=100, upload_to="image/%Y/%m", default="image/default.png")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name=u"验证码", max_length=20)
    email = models.EmailField(verbose_name=u"邮箱", max_length=50)
    send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register", u"注册"), ("forget", u"忘记密码")), max_length=15)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(verbose_name=u"标题", max_length=50)
    image = models.ImageField(verbose_name=u"轮播图", upload_to="banner/%Y/%m", max_length=100)
    url = models.URLField(verbose_name=u"访问地址", max_length=100)
    index = models.IntegerField(verbose_name=u"顺序", default=1)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
