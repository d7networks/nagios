# D7SMS for Nagios XI Configuration

Python script for sending SMS notifications from NagiosXI using D7SMS Gateway.

## Getting Started
These instructions will get you a copy of the script and configuration guidelines for setting it up in Nagios

## Prerequisites

1. Signup at [https://app.d7networks.com](https://app.d7networks.com/) and  verify account with mobile number
2. Navigate to API Tokens > Create App
3. Once the application is created, click on "Generate Token" and this token needs to be added in d7sms.py file. 

## Installation Instructions
### 1. Prepare 
1. Navigate to plugins folder on NagiosXI Server
2. Download d7sms.py from [https://github.com/d7networks/nagios/blob/master/d7sms.py](https://github.com/d7networks/nagios/blob/master/d7sms.py)
3. Replace "YOUR_D7_TOKEN" in the file with the token you have created earlier. 
4. Make it executable
```
          cd /usr/local/nagios/libexec/
          wget https://raw.githubusercontent.com/d7networks/nagios/master/d7sms.py
          chmod +x d7sms.py
```

### 2. Test the script
(Remeber to replace the destination number)

```
        ./d7sms.py --to 9715097526xx --content "Test message from Nagios"
```

### 3. Add notification commands

On Nagios XI  - GUI, Navigate to following path and add two commands seperately.   

Configure > Core Config Manager > Commands > Add new
```
Command Name:   service-notify-by-sms
command Line:   $USER1$/d7sms.py --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$:$SERVICEDESC$ on $HOSTNAME$ with IP $HOSTADDRESS$ Current State $SERVICESTATE$ Service Info: $SERVICEOUTPUT$ Date: $LONGDATETIME$"
Command Type:   misc command
Status:   Enabled (Active)

Command Name:   host-notify-by-sms
Command Line:   $USER1$/d7sms.py --to $CONTACTPAGER$ --content "$NOTIFICATIONTYPE$: Host: $HOSTNAME$, State: $HOSTSTATE$, Address: $HOSTADDRESS$, Info: $HOSTOUTPUT$, Date/Time: $LONGDATETIME$"
Command Type:   misc command
Status:   Enabled (Active)
```
<!-- ![alt text](https://d7networks.com/images/nagios/NagiosXI-1.png) -->

### 4. Update contact templates: 

Navigate to following path and add host, service notification commands to Assigned group for the templates you are using

```
Configure > Core Config Manager > Templates > Contact Templates
Click on generic contact/xi_contact_generic > Alert Settings > Manage host notification command 
Select host-notify-by-sms and click on Add selected
 
Click on generic contact/xi_contact_generic > Alert Settings > Manage service notification command
Select service-notify-by-sms and click on Add selected
```
![alt text](https://d7networks.com/images/nagios/NagiosXI-2.png)


### 5. Add contact to templates Used: 

```
Navigate to Configure > Core Config Manager > Templates > Host Templates
Click on the template used > Alert Settings > Manage Contacts > Select and add your contact from the list

Navigate to Configure > Core Config Manager > Templates > Service Templates
Click on the template used > Alert Settings > Manage Contacts > Select and add your contact from the list
```
![alt text](https://d7networks.com/images/nagios/NagiosXI-3.png)


### 6. Add pager number
```
Navigate to Configure > Core Config Manager > Alerting > Contacts

Select your contact > Add pager number and save
```
![alt text](https://d7networks.com/images/nagios/NagiosXI-4.png)

## Support and Help

You can get the latest version of this script from https://github.com/d7networks/nagios 

For all queries and help on installation please contact support@d7networks.com or visit https://d7networks.com

## Common queries and solutions: 
Q1: How to Limit number of notifications: 

Ans: There are two options you can follow to limit the notifications: 
     
     1. Setting the notification_interval directive in either the host or service definitions to 0. Doing this tells Nagios not to resend notifications for the same event. 
     
     2. Use Escalations. Here you can configure First / Last Notification and other related settings. This is available under "Configure > Core Config Manager > Alerting"
