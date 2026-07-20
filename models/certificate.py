from . import db


class Certificate(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150))

    issuer = db.Column(db.String(150))

    date = db.Column(db.String(50))