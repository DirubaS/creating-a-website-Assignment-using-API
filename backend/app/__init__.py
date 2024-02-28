from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
oauth = OAuth(app)

# Configure Google OAuth
google = oauth.remote_app(
    "google",
    base_url="https://www.google.com/accounts/",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    request_token_url=None,
    request_token_params={"scope": "email"},
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_method="POST",
    access_token_params=None,
    consumer_key="your-google-client-id",
    consumer_secret="your-google-client-secret",
)

# Import and register blueprints here (if applicable)
