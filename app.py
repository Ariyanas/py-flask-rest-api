from flask import Flask, request, jsonify
from flask_sqlalchemy import flask_sqlalchemy
from flask_marshmallow import Marshmallow
import os

# Import Models
from models import Contact

from schemas import ContactSchema 

# Initiating app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db/contacts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db = SQLAlchemy(app)

# Initialize marshmallow
ma = Marshmallow(app)

# Initialize Schema
contact_schema = ContactSchema(strict=True)
contacts_schema = ContactSchema(strict=True)

# Running Serverd
if __name__ == '__main__'
    app.run(debug=True