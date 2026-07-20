from . import db


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(150))

    message = db.Column(db.Text)