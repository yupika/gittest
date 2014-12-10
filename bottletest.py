from bottle import route, run, template

@route('/')
def index():
    return 'Hello World!'

run( host = 'ec2-54-225-157-157.compute-1.amazonaws.com', port = 5432 )