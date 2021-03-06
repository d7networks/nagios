# Nagios SMS Plugin

Python script for sending SMS notifications from Nagios using D7SMS Gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in Nagios

## Prerequisites

Before starting nagios setup Copy d7sms.py to nagios plugin folder make sure you have a valid subscription on https://d7networks.com. 

Please contact nagios@d7networks.com or signup at https://d7networks.com for FREE sms credits. 

## Installation Instructions
1. Nagios Setup


Copy d7sms.py to your nagios plugins folder and make it executable. You can download it from https://github.com/d7networks/nagios/blob/master/d7sms.py 

```
Following the location of plugins folder in different Operating Systems. 

Debian/Ubuntu: /usr/local/nagios/libexec
Centos: /usr/lib/nagios/plugins (32 bit)
        /usr/lib64/nagios/plugins (64 bit)
```

2. Create commands for SMS notification (Service notification and also host notification).
You can collect your API_Username and API_Password from https://d7networks.com and use it in the below commands. 

```
   Default path : /usr/local/nagios/etc/objects/commands.cfg
   define command{
       command_name    service-notify-by-sms
       command_line    $USER1$/d7sms.py --username API_Username --password API_Password --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$:$SERVICEDESC$ on $HOSTNAME$ with IP $HOSTADDRESS$ Current State $SERVICESTATE$ Service Info: $SERVICEOUTPUT$ Date: $LONGDATETIME$"
   }
   define command{
           command_name    host-notify-by-sms
           command_line    $USER1$/d7sms.py --username API_Username --password API_Password --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$: Host: $HOSTNAME$, State: $HOSTSTATE$, Address: $HOSTADDRESS$, Info: $HOSTOUTPUT$, Date/Time: $LONGDATETIME$"
       }
```


3. Update contact template and add below commands after existing host and service notification commands.

```
   Default path : /usr/local/nagios/etc/objects/templates.cfg
   service_notification_commands   notify-service-by-email,service-notify-by-sms
       host_notification_commands      notify-host-by-email,host-notify-by-sms
```

4. Add a pager number to your contacts, make sure it has the international prefix

## Support and Help

You can get the latest version of this script from https://github.com/d7networks/nagios 

For all queries and help on installation please contact nagios@d7networks.com or visit https://d7networks.com

Setup instructions for NagiosXI can be found here: https://github.com/d7networks/nagios/blob/master/Configure-NagiosXI.md
