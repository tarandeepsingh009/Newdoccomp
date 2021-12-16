import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def hello():
    return"Hello World!"

    connection = mysql.connectorconnect(
            user="user",password="pass", host="host"
            )
    cursor = connection.cursor()
    server.run()
