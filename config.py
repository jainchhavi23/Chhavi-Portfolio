import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

INSTANCE_FOLDER = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_FOLDER, exist_ok=True)


class Config:
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(INSTANCE_FOLDER, "portfolio.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False