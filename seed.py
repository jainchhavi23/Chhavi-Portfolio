from app import app
from models import db
from models.project import Project

with app.app_context():

    if Project.query.count() == 0:

        projects = [

            Project(
                title="CampusHub - Student Management System",
                description="A Flask-based Student Management System with CRUD operations, authentication and dashboard.",
                image="student-sphere.png",
                github="https://github.com/jainchhavi23",
                demo="#",
                featured=True
            ),

            Project(
                title="AI Resume Analyzer",
                description="An AI-powered Resume Analyzer that evaluates resumes and provides ATS-friendly suggestions.",
                image="ai-resume.png",
                github="https://github.com/jainchhavi23",
                demo="#",
                featured=False
            ),

            Project(
                title="Expense Tracker",
                description="A Python application to manage expenses and visualize spending records.",
                image="expense.png",
                github="https://github.com/jainchhavi23",
                demo="#",
                featured=False
            )
        ]

        db.session.add_all(projects)
        db.session.commit()

        print("✅ Projects added successfully!")

    else:
        print("⚡ Projects already exist in the database.")