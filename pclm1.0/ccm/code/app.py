from flask import Flask
from redis import Redis
import os
import urllib2

app = Flask(__name__)
redis = Redis(host='db2', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    jts = os.getenv("JTS")
    # response = urllib2.urlopen('http://10.0.2.15:8180')
    response = urllib2.urlopen(jts)
    html = response.read()
    return 'ccm version 1.0 called %s times - %s.' % (redis.get('hits'), html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9080, debug=True)
