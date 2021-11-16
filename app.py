import os
import json
import random
from flask import Flask, redirect, render_template, request, jsonify, json


app = Flask(__name__)
jokes = open('jokes.json', 'r').read()


@app.route("/")
def main():
    return random.choice(jokes)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
