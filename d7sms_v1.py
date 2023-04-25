#!/usr/bin/env python
# coding=utf-8

# Before starting nagios setup Copy d7sms.py to Nagios plugin folder make sure you have a valid subscription on https://d7networks.com.
# Please contact nagios@d7networks.com or signup at https://d7networks.com for FREE sms credits.

# ======== Installation Instructions ========

# 1. Nagios Setup
# Copy d7sms.py to your Nagios plugins folder and make it executable. You can download it from https://github.com/d7networks/nagios/blob/master/d7sms.py

# Following the location of plugins folder in different Operating Systems.

# Debian/Ubuntu: /usr/local/nagios/libexec
# Centos: /usr/lib/nagios/plugins (32 bit)
# /usr/lib64/nagios/plugins (64 bit)

# 2. Create commands for SMS notification (Service notification and also Host notification). You can collect your API_Username and API_Password from https://d7networks.com and use it in the below commands.

# Default path : /usr/local/nagios/etc/objects/commands.cfg
# define command{
# command_name service-notify-by-sms
# command_line $USER1$/d7sms.py --username API_Username --password API_Password--to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$:$SERVICEDESC$ on $HOSTNAME$ with IP $HOSTADDRESS$ Current State $SERVICESTATE$ Service Info: $SERVICEOUTPUT$ Date: $LONGDATETIME$"
# }

# define command{
# command_name host-notify-by-sms
# command_line $USER1$/d7sms.py --username API_Username --password API_Password --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$: Host: $HOSTNAME$, State: $HOSTSTATE$, Address: $HOSTADDRESS$, Info: $HOSTOUTPUT$, Date/Time: $LONGDATETIME$"
# }

# 3. Update contact template and add following lines after existing host and service notification commands.

# Default path : /usr/local/nagios/etc/objects/contacts.cfg
# service_notification_commands notify-service-by-email,service-notify-by-sms
# host_notification_commands notify-host-by-email,host-notify-by-sms

# 4. Add a pager number to your contacts, make sure it has the international prefix


# ======== Support and Help ========

# You can get the latest version of this script from https://github.com/d7networks/nagios

# For all queries and help on installation please contact nagios@d7networks.com or visit https://d7networks.com

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