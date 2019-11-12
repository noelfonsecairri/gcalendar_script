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



pprint.pprint(my_data[100]['attendees'][0]['email'])

#pprint.pprint(len(my_data))
#print(type(my_data))

#pprint.pprint(result)
print(type(result))
pprint.pprint(result.keys())
print(len(result))

#pprint.pprint(my_data[18]['attendees'])

'''for x in my_data:
    if 'attendees' not in x.keys():
        continue
    elif x['attendees'][0]['email'] == 'l.delosreyes@irri.org':
        pprint.pprint(x)
'''


'''for x in my_data:
    if x['attendees'][0]['email'] == 'l.delosreyes@irri.org':
        print(len(x))'''


def mail_event_list(email):
    try:
        for x in my_data:
            if 'attendees' not in x.keys():
                pass
            elif x['attendees'][0]['email'] == email:
                pprint.pprint(x)
                print(len(x))
    except:
        print('we gon an error')

mail_event_list('k.quintos@irri.org')