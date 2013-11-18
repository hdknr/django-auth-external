'''
Provide WSGIAuthUserScript script file at  the virtualenv bin directory:

import sys,os
VENV=os.path.dirname(__file__)
activate_this = os.path.join(VENV,'activate_this.py')
execfile(activate_this,dict(__file__ =activate_this))
#
BASE_DIR='/home/hdknr/ve/v16/src/authx/web/app'
sys.path.insert(0,BASE_DIR)
sys.path.insert(0,os.path.dirname( BASE_DIR)) 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
#
from authx.auth import *
'''

__all__=['check_password', ]

import syslog,sys

def authuser(usr,pwd,groups=[]):

    from django.contrib.auth import authenticate
    u=authenticate(username=usr,password=pwd )
    if u == None:
        return False
    if len(groups) > 0 : 
        return u.groups.filter(name__in = groups).exists()
    return True

def check_password(environ, user, password):
    return authuser(user,password)

