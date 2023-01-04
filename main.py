import version
from flask import Flask, request, Response
version.increment_version(3)


app = Flask(__name__)

MAX_LEN = 100


@app.route("/", methods=["POST"])
def hello_world():
    return f"<p>Hello, World with a post!</p><h1>I'm at version : {version.get_version()}</h1>"


@app.route('/file', methods=["POST"])
def write_new_file():
    request_data = request.get_json()
    name: str = request_data.get("name")
    content: str = request_data.get("content")

    if not name.strip():
        return Response("Name can't be empty", status=400, mimetype='application/text')

    if not content.strip() or len(content) > MAX_LEN:
        return Response(f"Content must not be empty, or longer than {MAX_LEN} char", status=400, mimetype='application/text')

    try:
        with open(name, "a") as file:
            file.write(content)
    except Exception as e:
        return Response("An error occured\n"+str(e), status=500, mimetype='application/text')

    return Response(status=200)


@app.route('/file', methods=["GET"])
def read_file():
    request_params = request.args
    name = request_params.get("name")

    if not name:
        return Response("Can't find without a name parameter", status=400, mimetype='application/text')

    content = None
    try:
        with open(name, "r") as file:
            content = file.readlines()
    except Exception as e:
        return Response("An error occured\n"+str(e), status=500, mimetype='application/text')

    return content
