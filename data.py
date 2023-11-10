from flask import Flask, jsonify
from main import app


@app.route("/")

def index():
    return jsonify({"data":data, "message":"success"}),200

