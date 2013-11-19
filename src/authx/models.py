# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

import logging,traceback
logger = logging.getLogger(__name__)

ENCS=(
    ('sha1', 'Secure Hash Algorihm (SHA1)'),
    ('none','not encrypted (plain text)'),
    ('crypt', 'UNIX crypt() encryption'),
    ('scrambled', 'MySQL PASSWORD encryption'),
    ('md5', 'MD5 hashing'),
    ('aes', 'Advanced Encryption Standard (AES) encryption'),
)

class Basic(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField('Username',max_length="50",)
    password = models.CharField('Password',max_length="50",)
    enc = models.CharField('Encryption',max_length="10",choices=ENCS,default=ENCS[0][0],)
    salt =  models.CharField('Salt',max_length="50",)       #: not used


from django.contrib.auth.models import User
import hashlib

old_set_password = User.set_password

def set_password(user, raw_password):
    if user.id == None:
        user.save()

    try:
        # generate password for mod_auth_mysql  Basic Authentication
        # TODO: get algorighm from basi.enc

        basic,created = Basic.objects.get_or_create(user=user,username=user.username )
        basic.password = hashlib.sha1(raw_password).hexdigest()   
        basic.salt = "none"
        basic.save()
    except :
        map( lambda e:logger.error(e), traceback.format_exc().split('\n'))
            

    old_set_password(user, raw_password)

User.set_password = set_password
