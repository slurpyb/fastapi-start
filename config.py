import os
from dotenv import load_dotenv

load_dotenv() 

# config = dotenv_values(".env")

# PORT = 5400
# BIND = '0.0.0.0'
# WORKERS = 10
# RELOAD = False

PORT = os.getenv('PORT')
BIND = os.getenv('BIND')
WORKERS = os.getenv('WORKERS')
RELOAD = os.getenv('RELOAD')