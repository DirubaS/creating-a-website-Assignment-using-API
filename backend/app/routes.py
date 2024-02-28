from flask import redirect, url_for, session
from app import app, google

@app.route("/login")
def login():
    return google.authorize(callback=url_for("authorized", _external=True))

@app.route("/login/authorized")
def authorized():
    response = google.authorized_response()
    if response is None or response.get("access_token") is None:
        return "Access denied: reason={} error={}".format(
            request.args["error_reason"], request.args["error_description"]
        )
    session["access_token"] = (response["access_token"], "")
    user_info = google.get("userinfo")
    # Process user info and log in the user
    # ...

@google.tokengetter
def get_google_oauth_token():
    return session.get("access_token")
