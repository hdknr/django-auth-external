# -*- coding: utf-8 -*-
from django.utils.timezone import datetime
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from . import GenericCommand
import os,sys

import logging,traceback
logger = logging.getLogger(__name__)

class Command(GenericCommand):

    def handle_default(self,*args,**options):
        if os.environ.get('AUTHTYPE','') == 'GROUP':
            return self.handle_gropu(*args,**options) 
        return self.handle_auth(*args,**options)

    def handle_auth(self,*args,**options):
        code=-1
        try:
            user = authenticate(username=os.environ['USER'], 
                            password=os.environ['PASS'] )
            
            logger.debug("AUTH USER : %(USER)s " % os.environ  )
            code = 0 if user else -1 
        except:
            logger.error( traceback.format_exc() )
        
        return sys.exit( code )

    def handle_group(self,*args,**options):
        code=-1
        try:
            if all([options['data'] ,
                        type(options['data'])==file,
                            not options['data'].isatty()  ]):
                user,groups = [ i.replace("\n","") for i in options['data'].readlines() ][:2]
                logger.debug("GROUP USER : %s , GROUPS : %s" % (user,groups)  )
                if Group.objects.filter(user__username=user,
                            name__in = groups.split(' ') ).exists():  
                    code=0
        except:
            logger.error( traceback.format_exc() )
        return sys.exit( code )


