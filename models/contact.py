class Contact(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email) :
        self.name = name
        self.email = email