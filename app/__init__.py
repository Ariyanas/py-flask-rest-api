from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initiating app
app = Flask(__name__)

# Database
app.config.from_object('config')

# Initialize DB
db = SQLAlchemy(app)

# Initialize marshmallow
ma = Marshmallow(app)

# Routes, Models & Schema registration
from . import routes, schemas, models

# HTTP Error Handling
@app.errorhandler(404) 
def not_found(error):
    return jsonify(success = False, message='Resource Not Found' )


# Build the DB
db.create_all()