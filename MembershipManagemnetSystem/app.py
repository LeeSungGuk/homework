import logging as log

from flask import Flask, request, make_response

log.basicConfig(level=log.DEBUG)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register', methods=['POST'])
def register():
    log.debug("Register Get")
    input_json = request.get_json(silent=True)
    log.debug("input data: {}".format(input_json))

    # return make_response(input_json)
    return ""



if __name__ == '__main__':
    app.run(debug=True)
