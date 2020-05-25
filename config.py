#!python3 config.py

import os

os.system("python3 -m venv venv")
if os.path.isdir("venv"):
    if os.path.isdir("venv/Scripts"):
        # windows
        os.system("venv\\Scripts\\pip.exe install -r requirements.txt")
        print('\n\nConfigured for windows. Activating venv...')
        os.system("cmd.exe /K venv\\Scripts\\activate.bat")

    elif os.path.isdir("venv/bin"):
        # linux
        os.system("venv\\bin\\pip.exe install -r requirements.txt")
        print('\n\nConfigured for linux. Activating venv...')
        os.system("venv\\bin\\activate")

    else:
        print('What version of venv is this, missing sub dirs')
        exit(1)
else:
    print("Couldn't create venv, try apt install python3-venv")
    exit(2)