# Nagios SMS Plugin

Python script for sending SMS notifications from Nagios using D7SMS Gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in Nagios

## Prerequisites

1. Signup at [https://app.d7networks.com](https://app.d7networks.com/) and  verify account with mobile number
2. Navigate to Developer > Application > Create App
3. Once the application is created, click on "Generate Token" and this token needs to be added in d7sms.py file. 

Please contact support@d7networks.com or signup at https://d7networks.com for FREE sms credits. 

## Installation Instructions
1. Download d7sms.py from [https://github.com/d7networks/nagios/blob/master/d7sms.py](https://github.com/d7networks/nagios/blob/master/d7sms.py)
2. Replace "YOUR_D7_TOKEN" in the file with the token you have created earlier. 
3. Copy d7sms.py to your nagios plugins folder and make it executable

```
Following the location of plugins folder in different Operating Systems. 

Debian/Ubuntu: /usr/local/nagios/libexec
Centos: /usr/lib/nagios/plugins (32 bit)
        /usr/lib64/nagios/plugins (64 bit)
```

4. Create commands for SMS notification (Service notification and also host notification).
You can collect your API_Username and API_Password from https://d7networks.com and use it in the below commands. 

```
   Default path : /usr/local/nagios/etc/objects/commands.cfg
   define command{
       command_name    service-notify-by-sms
       command_line    $USER1$/d7sms.py --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$:$SERVICEDESC$ on $HOSTNAME$ with IP $HOSTADDRESS$ Current State $SERVICESTATE$ Service Info: $SERVICEOUTPUT$ Date: $LONGDATETIME$"
   }
   define command{
           command_name    host-notify-by-sms
           command_line    $USER1$/d7sms.py --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$: Host: $HOSTNAME$, State: $HOSTSTATE$, Address: $HOSTADDRESS$, Info: $HOSTOUTPUT$, Date/Time: $LONGDATETIME$"
       }
```


5. Update contact template and add below commands after existing host and service notification commands.

```
   Default path : /usr/local/nagios/etc/objects/templates.cfg
   service_notification_commands   notify-service-by-email,service-notify-by-sms
       host_notification_commands      notify-host-by-email,host-notify-by-sms
```

6. Add a pager number to your contacts, make sure it has the international prefix

## Support and Help

You can get the latest version of this script from https://github.com/d7networks/nagios 

For all queries and help on installation please contact nagios@d7networks.com or visit https://d7networks.com

Setup instructions for NagiosXI can be found here: https://github.com/d7networks/nagios/blob/master/Configure-NagiosXI.md
