from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)