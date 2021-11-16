import os
import json
import random
import jokes
from flask import Flask, redirect, render_template, request, jsonify, json


app = Flask(__name__)


@app.route("/")
def main():
    return random.choice(jokes.jokes)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
