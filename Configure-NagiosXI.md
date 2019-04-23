# D7SMS for Nagios XI Configuration

Python script for sending SMS notifications from NagiosXI using D7SMS Gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in Nagios

## Prerequisites

Before starting make sure you have a valid subscription on https://d7networks.com.    
Please contact nagios@d7networks.com or signup at https://d7networks.com for FREE sms credits. 

## Installation Instructions
1. Nagios Setup   

Copy d7sms.py to your nagios plugins folder and make it executable
```
cd /usr/local/nagios/libexec/
wget https://raw.githubusercontent.com/d7networks/nagios/master/d7sms.py
chmod +x d7sms.py
```

2. Test extension
```
./d7sms.py --username API_Username --password API_Password --to Mobile_Number --content "test"
```

3. Add notification commands

Procedure: On Nagios XI  - GUI, Navigate to following path and add two commands seperately.   
Important: Here you must replace API_Username and API_Password with the one you recieved from our website.    
Configure > Core Config Manager > Commands > Add new
```
Command Name:   service-notify-by-sms
command Line:   $USER1$/d7sms.py --username API_Username --password API_Password --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$:$SERVICEDESC$ on $HOSTNAME$ with IP $HOSTADDRESS$ Current State $SERVICESTATE$ Service Info: $SERVICEOUTPUT$ Date: $LONGDATETIME$"
Command Type:   misc command
Status:   Enabled

Command Name:   host-notify-by-sms
Command Line:   $USER1$/d7sms.py --username API_Username --password API_Password --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$: Host: $HOSTNAME$, State: $HOSTSTATE$, Address: $HOSTADDRESS$, Info: $HOSTOUTPUT$, Date/Time: $LONGDATETIME$"
Command Type:   misc command
Status:   Enabled
```
![alt text](https://d7networks.com/images/nagios/NagiosXI-1.png)

4. Update contact templates: 

Procedure: 
Navigate to following path and add host, service notification commands to Assigned group for the templates you are using

```
Configure > Core Config Manager > Templates > Contact Templates
Click on generic contact/xi_contact_generic > Alert Settings > Manage host notification command 
Select host-notify-by-sms and click on Add selected
 
Click on generic contact/xi_contact_generic > Alert Settings > Manage service notification command
Select service-notify-by-sms and click on Add selected
```
![alt text](https://d7networks.com/images/nagios/NagiosXI-2.png)


5. Add contact to templates Used: 

```
Procedure: 
Navigate to Configure > Core Config Manager > Templates > Host Templates
Click on the template used > Alert Settings > Manage Contacts > Select and add your contact from the list

Navigate to Configure > Core Config Manager > Templates > Service Templates
Click on the template used > Alert Settings > Manage Contacts > Select and add your contact from the list
```
![alt text](https://d7networks.com/images/nagios/NagiosXI-3.png)


6. Add pager number
```
Procedure: 

Navigate to Configure > Core Config Manager > Alerting > Contacts

Select your contact > Add pager number and save
```
![alt text](https://d7networks.com/images/nagios/NagiosXI-4.png)

## Support and Help

You can get the latest version of this script from https://github.com/d7networks/nagios 

For all queries and help on installation please contact nagios@d7networks.com or visit https://d7networks.com

## Common queies and solutions: 
Q1: How to Limit number of notifications: 

Ans: There are two options you can follow to limit the notifications: 
     
     1. Setting the notification_interval directive in either the host or service definitions to 0. Doing this tells Nagios not to resend notifications for the same event. 
     
     2. Use Escalations. Here you can configure First / Last Notification and other related settings. This is available under "Configure > Core Config Manager > Alerting"
