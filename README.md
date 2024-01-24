# Nagios SMS Plugin

Python script for sending SMS notifications from Nagios using D7SMS Gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in Nagios

## Prerequisites

1. Signup at [https://app.d7networks.com](https://app.d7networks.com/) and  verify account with mobile number
2. Navigate to API Tokens > Create App
3. Once the application is created, click on "Generate Token" and this token needs to be added in d7sms.py file. 

## Installation Instructions

### Download script and configure Token

1. Navigate to plugins folder on Nagios/Icinga Server
```
        Following the location of plugins folder in different Operating Systems. 

        Debian/Ubuntu: /usr/local/nagios/libexec
        Centos: /usr/lib/nagios/plugins (32 bit)
                /usr/lib64/nagios/plugins (64 bit)
```
2. Download d7sms.py from [https://github.com/d7networks/nagios/blob/master/d7sms.py](https://github.com/d7networks/nagios/blob/master/d7sms.py)
3. Make it executable
```
        cd /usr/local/nagios/libexec
        wget https://raw.githubusercontent.com/d7networks/nagios/master/d7sms.py
        chmod +x d7sms.py
```
4. Replace "YOUR_D7_TOKEN" in the file with the token you have created earlier. 
```
        vim d7sms.py +54
```
### Test the script
(Remeber to replace the destination number)

```
        ./d7sms.py --to 9715097526xx --content "Test message from Nagios"
```

### Modify Nagios configs

1. Create notification commands.
    
    Create for both Service and Host notifications. 

    Default path : /usr/local/nagios/etc/objects/commands.cfg
```
define command{
        command_name    service-notify-by-sms
        command_line    $USER1$/d7sms.py --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$:$SERVICEDESC$ on $HOSTNAME$ with IP $HOSTADDRESS$ Current State $SERVICESTATE$ Service Info: $SERVICEOUTPUT$ Date: $LONGDATETIME$"
}
define command{
        command_name    host-notify-by-sms
        command_line    $USER1$/d7sms.py --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$: Host: $HOSTNAME$, State: $HOSTSTATE$, Address: $HOSTADDRESS$, Info: $HOSTOUTPUT$, Date/Time: $LONGDATETIME$"
        }
```

2. Update contact template 

    Add below commands to templates. 
    
    Default path : /usr/local/nagios/etc/objects/templates.cfg
```
        service_notification_commands   notify-service-by-email,service-notify-by-sms
        host_notification_commands      notify-host-by-email,host-notify-by-sms
```

3. Add a pager number to your contacts. 
        
    This will be used as sms destination number. Make sure it has the international prefix (country code)
    
    Default path : /usr/local/nagios/etc/objects/contacts.cfg

```
        define contact {
            contact_name            nagiosadmin
            use                     generic-contact
            alias                   Nagios Admin
            email                   xyz@d7networks.com
            pager                   +9715097526xx
        }
```

4. Check configurations and restart Nagios

5. Also, you can check the /usr/local/nagios/nagios.log, in case if you need to check for errors

## Support and Help

You can get the latest version of this script from https://github.com/d7networks/nagios 

For all queries and help on installation please contact support@d7networks.com or visit https://d7networks.com

Setup instructions for NagiosXI can be found here: https://github.com/d7networks/nagios/blob/master/Configure-NagiosXI.md
