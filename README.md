# Nagios SMS Plugin

Python script for sending SMS notifications in nagios using direct7 sms gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in nagios

## Prerequisites

Before starting nagios setup Copy d7sms.py to Nagios plugin folder make sure you have a valid subscription on http://sms.d7networks.com. Please contact support@d7networks.com if you need to test the plugin.


### Nagios Setup


Copy d7sms.py to your Nagios plugin folder and make it executable.

```
Debian/Ubuntu: /usr/local/nagios/libexec
Centos: /usr/lib/nagios/plugins (32 bit)
        /usr/lib64/nagios/plugins (64 bit)
```

Create commands for SMS notification (Service notification and also host notification).
Replace USER and PASS with the credentials recieved from  http://sms.d7networks.com


```
   Default path : /usr/local/nagios/etc/objects/commands.cfg
   define command{
       command_name    service-notify-by-sms
       command_line    $USER1$/d7sms.py --username USER --password PASS --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$:$SERVICEDESC$ on $HOSTNAME$ with IP $HOSTADDRESS$ Current State $SERVICESTATE$ Service Info: $SERVICEOUTPUT$ Date: $LONGDATETIME$"
   }
   define command{
           command_name    host-notify-by-sms
           command_line    $USER1$/d7sms.py --username USER --password PASS --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$: Host: $HOSTNAME$, State: $HOSTSTATE$, Address: $HOSTADDRESS$, Info: $HOSTOUTPUT$, Date/Time: $LONGDATETIME$"
       }
```


Update contact template and add below commands after existing host and service notification commands.

```
   Default path : /usr/local/nagios/etc/objects/contacts.cfg
   service_notification_commands   notify-service-by-email,service-notify-by-sms
       host_notification_commands      notify-host-by-email,host-notify-by-sms
```

Add a pager number to your contacts, make sure it has the international prefix

you can get the latest version of this script from 
GUTHUB : https://github.com/d7networks/nagios

For all queries and help on installation please contact support@d7networks.com