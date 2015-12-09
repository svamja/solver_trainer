#!/usr/bin/python
from bottle import route, response, hook, run, get, post, request

import slidingpuzzle

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'

@route('/hello')
def hello():
    return "Hello World!"

@route('/slidingpuzzle', method=['OPTIONS', 'POST'])
def post_slidingpuzzle():
    if request.method == 'OPTIONS':
        return {}
    data = request.json
    print(data)
    response = slidingpuzzle.solve_matrix(data["matrix"])
    return response

run(host='localhost', port=8001, debug=True, reloader=True)
