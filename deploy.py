import os
import time

# shutdown all containers
os.system("docker-compose stop")

# start all containers
os.system("docker-compose up -d")