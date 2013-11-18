# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Basic(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField('UserNmae',max_length="20",)
    password = models.CharField('Password',max_length="50",)
