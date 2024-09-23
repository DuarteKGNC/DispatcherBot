import requests
import json
from decouple import config
from .tickets_helper import ticket_skeleton
from time import sleep

# INITIAL CONFIG VARS
TOKEN = config("TOKEN")
SUPPORT_CHANNEL_ID = config("SUPPORT_CHANNEL_ID")
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}
# ENDPOINTS
SEND_TEXT_ENDPOINT = "https://slack.com/api/chat.postMessage"
GET_IDS_ENDPOINT = "https://slack.com/api/users.list"
UPLOAD_FILES = "https://slack.com/api/files.upload"

def get_ids(): # Get the IDs of all users
    sleep(1.5)
    response = requests.get(GET_IDS_ENDPOINT, headers=HEADERS)
    users = {}
    for i in response.json()['members']:
        users[i['name']] = i['id']
    return users

def dispatch(ticket):
    data = ticket_skeleton(ticket, ticket['fields']['goalkeeper'], SUPPORT_CHANNEL_ID)
    response = requests.post(SEND_TEXT_ENDPOINT, headers=HEADERS, data=json.dumps(data))
    return response.json()