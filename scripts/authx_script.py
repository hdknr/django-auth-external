''' 
'''
if __name__ == '__main__':
    import sys,os
    import traceback
    if len(sys.argv) < 2:
        sys.stderr.write('you need path of your django application')
        sys.exit(1) 

    #: django path
    sys.argv[1] = os.path.abspath( sys.argv[1]  )
    sys.path.append(os.path.dirname(sys.argv[1]))  
    sys.path.append(sys.argv[1]) 

    #: argv[1] is manage.py command 
    sys.argv[1] = os.path.basename( __file__ )

    from django.core.management import execute_manager
    import imp
    try:
        imp.find_module('settings') # Assumed to be in the same directory.
    except ImportError:
        import sys
        sys.stderr.write(str(sys.path))
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
        sys.exit(1)
    
    import settings
    
    try:
        execute_manager(settings)
    except:
        print traceback.format_exc() 
