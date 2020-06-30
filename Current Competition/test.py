from LHFE import lhfe
import shutil
import os

CURRENT = 'current'
NEW = 'new'
TEST = 'test'
KEEP = '.gitkeep'
try:
    shutil.rmtree(CURRENT)
except:
    pass
os.mkdir(CURRENT)
open(os.path.join(CURRENT, KEEP), 'w').close()
try:
    shutil.rmtree(NEW)
except:
    pass
os.mkdir(NEW)
files = [file for file in os.scandir(TEST)]
files.sort(key=os.path.getctime)
for file in files:  # type: os.DirEntry
    shutil.copy(file.path, NEW)
open(os.path.join(NEW, KEEP), 'w').close()
lhfe.start(True)
