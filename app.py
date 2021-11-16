from flask import Flask, redirect, render_template, request, jsonify, json


app = Flask(__name__)


@app.route("/")
def main():
    return "Thanks for using this api By @DKBOTZ"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
