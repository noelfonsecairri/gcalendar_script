#!/usr/bin/env python3

from googleapiclient.discovery import build

service = build('calendar', 'v3')


collection = service.stamps()

request = collection.list(cents = 5)
print(request)