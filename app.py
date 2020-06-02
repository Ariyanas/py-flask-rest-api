from flask import Flask, request, jsonify
from flask_sqlalchemy import flask_sqlalchemy
from flask_marshmallow import Marshmallow

# Initiating app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({ message: 'Hello From FLASK REST API !' })

# Running Server
if __name__ == '__main__'
    app.run(debug=True