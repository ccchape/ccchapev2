from bottle import route, run, template, view

from bottle import static_file
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/')
@view("index")
def index():
    return {}

run(host='localhost', port=8080, reloader=True)
