import os
import time

cmd="gunicorn -w 1 app:app -b=0.0.0.0:8000"
os.system(cmd)