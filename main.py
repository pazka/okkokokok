import version
from Worker import Worker
from Room import Room

version.increment_version(3)

from flask import Flask

app = Flask(__name__)


@app.route("/",methods=["POST"])
def hello_world():
    return f"<p>Hello, World with a post!</p><h1>I'm at version : {version.get_version()}</h1>"
