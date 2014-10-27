from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host='db2', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'JTS version 1.0 called %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9080, debug=True)
