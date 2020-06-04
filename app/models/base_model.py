from app import db

# Base Model for the app which will have all the common columns
class BaseModel(db.Model):
    __abstract__ = True

    # Timestamps
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())