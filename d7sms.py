#!/usr/bin/env python
# coding=utf-8

# Before starting nagios setup Copy d7sms.py to Nagios plugin folder make sure you have a valid subscription on http://sms.d7networks.com. Please contact support@d7networks.com if you need to test the plugin.

#------------------ Nagios Setup -------------------


# Copy d7sms.py to your Nagios plugin folder and make it executable.

#  Debian/Ubuntu: /usr/local/nagios/libexec
#  Centos: /usr/lib/nagios/plugins (32 bit)
#          /usr/lib64/nagios/plugins (64 bit)


# Create commands for SMS notification (Service notification and also host notification).
#  Replace USER and PASS with the credentials recieved from  http://sms.d7networks.com

#   Default path : /usr/local/nagios/etc/objects/commands.cfg
#   define command{
#       command_name    service-notify-by-sms
#       command_line    $USER1$/d7sms.py --username USER --password PASS --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$:$SERVICEDESC$ on $HOSTNAME$ with IP $HOSTADDRESS$ Current State $SERVICESTATE$ Service Info: $SERVICEOUTPUT$ Date: $LONGDATETIME$"
#   }
#   define command{
#           command_name    host-notify-by-sms
#           command_line    $USER1$/d7sms.py --username USER --password PASS --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$: Host: $HOSTNAME$, State: $HOSTSTATE$, Address: $HOSTADDRESS$, Info: $HOSTOUTPUT$, Date/Time: $LONGDATETIME$"
#        }

#Update contact template and add below commands after existing host and service notification commands.

#   Default path : /usr/local/nagios/etc/objects/contacts.cfg
#   service_notification_commands   notify-service-by-email,service-notify-by-sms
#       host_notification_commands      notify-host-by-email,host-notify-by-sms


# Add a pager number to your contacts, make sure it has the international prefix
#you can get the latest version of this script from GUTHUB : https://github.com/d7networks/nagios
# For all queries and help on installation please contact support@d7networks.com

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--username', help='D7 sms gateway username')
parser.add_argument('--password', help='D7 sms gateway password')
parser.add_argument('--source_address', help='D7 sms gateway password')
parser.add_argument('--to', help='SMS receivers mobile numbers, eg: 9715090xx, 9734565xx')
parser.add_argument('--content', help='Message content to be send')

if __name__ == '__main__':
    version = sys.version
    if version[:1] == '2':
        from urllib2 import urlopen
        from urllib import urlencode
    elif version[:1] == '3':
        from urllib.request import urlopen
        from urllib.parse import urlencode
    args = parser.parse_args()
    if not (args.username and  args.password and args.to and args.content) :
        print("--username, --password ,--to and --content arguments are required to send sms")
    else:
        if args.source_address :
            source_address = args.source_address
        else:
            source_address = 'd7-nag'
        username = args.username.strip('\'')
        password = args.password.strip('\'')
        content =  args.content.strip('\'')
        to = args.to.strip('\'').split(',') # will be a list of destinations
        for destination in to:
            baseParams = {
                'username': username,
                'password': password,
                'from': source_address,
                'to': destination,
                'content': content
            }
            # Send an SMS-MT to d7 sms gateway
            urlopen("http://smsc.d7networks.com:1401/send?%s" % urlencode(baseParams)).read()
