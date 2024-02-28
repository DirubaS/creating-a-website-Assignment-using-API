from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    User model to store user details.
    """
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Admin or Employee
    oauth_token = db.Column(db.String(500), nullable=False)  # Store OAuth token

class DailySteps(db.Model):
    """
    DailySteps model to store daily step counts.
    """
    step_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    step_count = db.Column(db.Integer, nullable=False)

# Other models (if needed) can be added here

# Initialize the database
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
