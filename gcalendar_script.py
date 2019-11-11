#!/usr/bin/env python3

import pprint, pickle, json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ["https://www.googleapis.com/auth/calendar"]
flow = InstalledAppFlow.from_client_secrets_file(
    "irri_google_calendar_credentials.json", scopes=scopes
)
credentials = flow.run_local_server()


pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()
# pprint.pprint(result['items'][0])

calendar_id = result["items"][0]["id"]
result = service.events().list(calendarId=calendar_id, timeZone="Asia/Manila").execute()


my_data = result["items"]


pprint.pprint(my_data[100])




for x in my_data:
    if my_data[x]['attendees']['email'] == 'l.delosreyes@irri.org':
        print(x['description'])

"""    for i in x['attendees']:
        if i['email'] == 'l.delosreyes@irri.org':
            print(my_data[x]['description'])"""
             