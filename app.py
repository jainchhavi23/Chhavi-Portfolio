from flask import Flask, render_template
from config import Config
from models import db
from models.project import Project

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():

    projects = Project.query.all()

    return render_template(
        "index.html",
        projects=projects
    )


if __name__ == "__main__":
    app.run(debug=True)