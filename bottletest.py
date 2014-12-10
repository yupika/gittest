from bottle import route, run, template
import os

@route('/')
def index():
    return 'Hello World!'

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))