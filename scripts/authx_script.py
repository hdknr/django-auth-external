''' 
'''
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

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
