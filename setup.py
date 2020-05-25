#!python3 setup.py
import os
from sys import argv
os.chdir(os.path.dirname(sys.argv[0]))
no_shell = 'no-shell' in argv
os.system("python3 -m venv venv")
if os.path.isdir("venv"):
    if os.path.isdir("venv/Scripts"):
        # windows
        os.system("venv\\Scripts\\pip.exe install -r requirements.txt")
        print('\n\nConfigured for windows.')
        if not no_shell:
            os.system("cmd.exe /K venv\\Scripts\\activate.bat")

    elif os.path.isdir("venv/bin"):
        # linux
        os.system("venv/bin/pip install -r requirements.txt")
        print('\n\nConfigured for linux.')
        if not no_shell:
            os.system("/bin/bash --rcfile venv/bin/activate")

    else:
        print('What version of venv is this, missing sub dirs')
        exit(1)
else:
    print("Couldn't create venv, try apt install python3-venv")
    exit(2)
