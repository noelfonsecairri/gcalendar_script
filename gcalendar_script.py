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


#pprint.pprint(result['items'][0])
pprint.pprint(result['items'][0]['id'])
pprint.pprint(result['items'][1]['id'])
#print(result.keys())


#getting data from single calendar ID
calendar_id = result["items"][1]["id"]
result = service.events().list(calendarId=calendar_id, timeZone="Asia/Manila").execute()
#pprint.pprint(result)
print(result.keys())
print(result['items'][-1].values())
last_item = result['items'][-1].items()

print(result['items'][-1]['id'])

for x in last_item:
    print(x)



#get data from multiple calendar IDs

'''my_data = result['items']

for x in my_data:
    for i in x[0]['id']:
        if i == 'njfonseca@gmail.com':
            calendar_id = 
'''

########################

#my_data = result["items"]

'''pprint.pprint(result)
pprint.pprint(len(result))
pprint.pprint(type(result))'''

'''def mail_event_list(email):
    #try:
        for x in my_data:
            if 'attendees' not in x.keys():
                pass
            elif x['attendees'][0]['email'] == email:
                #pprint.pprint(x['created'])
                #print(x.keys())
                #pprint.pprint(x)
                print(x)

    #except:
        #print('we got an error')

mail_event_list('n.fonseca@irri.org')'''
