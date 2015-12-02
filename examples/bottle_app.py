from bottle import route, run

import slidingpuzzle

@route('/hello')
def hello():
    return "Hello World!"

@route('/solve')
def solve():
    matrix = range(16)
    matrix[14], matrix[15] = matrix[15], matrix[14]
    response = slidingpuzzle.solve_matrix(matrix)
    return response

run(host='localhost', port=8001, debug=True, reloader=True)
