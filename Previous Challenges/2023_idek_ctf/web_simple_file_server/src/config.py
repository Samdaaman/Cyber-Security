import random
import os
import time

SECRET_OFFSET = 0 # REDACTED
seed = round((time.time() + SECRET_OFFSET) * 1000)
print(seed)
random.seed(seed)
os.environ["SECRET_KEY"] = "".join([hex(random.randint(0, 15)) for x in range(32)]).replace("0x", "")
