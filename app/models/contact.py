from app import db
from .base_model import BaseModel

class Contact(BaseModel):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email