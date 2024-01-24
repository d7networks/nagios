#!/usr/bin/python3
# coding=utf-8

import argparse
import sys
import json
import urllib.request

GW_URL = "https://api.d7networks.com/messages/v1/send"

# can be generated from https://app.d7networks.com/developer/applications'
D7TOKEN = "YOUR_D7_TOKEN"

parser = argparse.ArgumentParser()
parser.add_argument('--source_address', help='SMS sender name, eg: nag-alert')
parser.add_argument(
    '--to', help='SMS receivers mobile numbers, eg: 9715090xx, 9734565xx')
parser.add_argument('--content', help='Message content to be send')

if __name__ == '__main__':
    args = parser.parse_args()
    print("Arguments received:")
    print(args)
    if not (args.to and args.content):
        print("--to and --content arguments are required to send sms")
    else:
        if args.source_address:
            source_address = args.source_address
        else:
            source_address = 'd7-nag'
        content = args.content.strip('\'')
        to = args.to.strip('\'').replace(' ','').split(',')  # will be a list of destinations
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + D7TOKEN
        }
        message_globals = {
            "originator": source_address,
        }
        messages = [ 
            {
                "recipients":to,
                "content": content,
                "msg_type": "text",
                "data_coding": "text"
            } 
        ]
        
        json_data = json.dumps({
            "message_globals": message_globals,
            "messages": messages
        })
        
        
        req = urllib.request.Request(GW_URL, data=json_data.encode('utf-8'), headers=headers)
        try:
            response = urllib.request.urlopen(req, timeout=10)
        except urllib.error.HTTPError as e:
            print(f"Failed to send sms, reason: {e.reason}, code: {e.code} ")
        else:
            response_data = response.read().decode('utf-8')
            print(response_data)