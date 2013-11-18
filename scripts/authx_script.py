''' 
'''
import inspect
def info(msg):
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    print frm
    print '[%s] %s' % (mod.__name__, msg)

import sys
import syslog

def check_password(environ, user, password):
    syslog.openlog(sys.argv[0], syslog.LOG_PID|syslog.LOG_PERROR, syslog.LOG_LOCAL0)
    for p in sys.path:
        syslog.syslog(syslog.LOG_INFO, '@@@@'+ p )
    return True


if __name__ == '__main__':
    import sys,os
    import traceback
    if len(sys.argv) < 2:
        sys.stderr.write('you need path of your django application')
        sys.exit(1) 

    #: django path
    settings_path = os.path.abspath( sys.argv[1]  )
    BASE_DIR = os.path.dirname(settings_path) 

    sys.path.insert(0, os.path.dirname( BASE_DIR ) )
    sys.path.insert(0, BASE_DIR )

    os.environ.setdefault("DJANGO_SETTINGS_MODULE",  
            ".".join( settings_path.rsplit('.')[0].split('/')[-2:]) )

    sys.argv.pop(1)
    if len(sys.argv) < 2:
        sys.argv.append('authn')            #:defautl command

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
