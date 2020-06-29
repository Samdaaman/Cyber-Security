from LHFE.lhfe import LHFE
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
shutil.copytree(TEST, NEW)
open(os.path.join(NEW, KEEP), 'w').close()
LHFE.start(True)
