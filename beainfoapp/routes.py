import datetime, random
from flask import request, jsonify
from datetime import timedelta, datetime

from beainfoapp import app


@app.route("/")
def home():
    return "home"


today = datetime.now()

def current_time():
    current_time = datetime.utcnow()
    # Generate a random offset in seconds (-2 to +2 minutes)
    
    return current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

@app.route("/api", methods=['GET'],)
def user():
    args = request.args
    slack_name = args.get("slack_name")
    track = args.get("track")

    if slack_name and track:
        user_data = {
            "slack_name": slack_name,
            "current_day": today.strftime('%A'),
            "utc_time": current_time(),
            "track": track,
            "github_file_url": "https://github.com/Bea-3/backend_taskone/blob/main/beainfoapp/routes.py",
            "github_repo_url": "https://github.com/Bea-3/backend_taskone/tree/main",
            "Status_code": 200
        }
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "information required", "Status_code": 400}), 400