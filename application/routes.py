from application import app
from flask import jsonify, request
from .controllers import index, create, show, patch, delete

@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome to the Friends Catchphrase API"
    }), 200

@app.route("/characters", methods=["GET", "POST"])
def handle_character():
    if request.method == "GET":
        return index()
    
    if request.method == "POST":
        return create()

@app.route("/characters/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show_character(id):
    if request.method == "GET":
        return show(id)

    if request.method == "PATCH":
        return patch(id)

    if request.method == "DELETE":
        return delete(id)