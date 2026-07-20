from . import db


class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text, nullable=False)

    image = db.Column(db.String(200))

    github = db.Column(db.String(250))

    demo = db.Column(db.String(250))

    featured = db.Column(db.Boolean, default=False)