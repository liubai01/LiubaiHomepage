import os
import time

cmd="gunicorn --certfile=server.crt --keyfile=server.key -w 1 app:app -b=0.0.0.0:8000"

while True:
    if not (os.path.exists("server.crt") and os.path.exists("server.key")):
        time.sleep(1)
    else:
        break
os.system(cmd)