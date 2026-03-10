import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load credentials from .env
load_dotenv()

def get_zoom_token():
    """Fetch an OAuth access token from Zoom"""
    url = "https://zoom.us/oauth/token"
    auth = HTTPBasicAuth(os.getenv("ZOOM_CLIENT_ID"), os.getenv("ZOOM_CLIENT_SECRET"))
    params = {
        "grant_type": "account_credentials",
        "account_id": os.getenv("ZOOM_ACCOUNT_ID")
    }
    response = requests.post(url, auth=auth, params=params)
    response.raise_for_status()
    token = response.json().get("access_token")
    return token


def create_zoom_meeting(topic, start_time, duration=30):
    """Create a new Zoom meeting"""
    token = get_zoom_token()
    url = "https://api.zoom.us/v2/users/me/meetings"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "topic": topic,
        "type": 2,  # scheduled meeting
        "start_time": start_time,  # format: "2025-11-09T15:00:00Z"
        "duration": duration,
        "timezone": "Asia/Kolkata",
        "settings": {
            "host_video": True,
            "participant_video": True,
            "join_before_host": False,
            "mute_upon_entry": True
        }
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()
