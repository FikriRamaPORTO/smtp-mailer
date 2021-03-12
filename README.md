# Automate sending mass emails
Using Python's libraries, we want to construct a script that can collect contacts' emails, attachments, names, and personal identifiable information (PII) to be temporarily stored and sent in a mass email.

## Connect to our email server
To connect to our email server, we can use the smtp library to send emails and the EmailMessage package to hold content for our data. SMTP can use SSL if need be, and can use domain servers to connect our emails. Note that SMTP ports are traditionally 587, however, if we are implementing SSL, our port is 465. 
``
```
os.getcwd() 
# SMTP - port: 587
# SMTP_SSL - port: 465
python -m smtpd -c DebuggingServer -n localhost:1025
```

### Testing using Local Host
```
# constants
site_code = "au.dcap.dep"
receiver = "ggian205@aol.com"

# Get environment details
EMAIL_ADDRESS = config('EMAIL_USER')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')

msg = EmailMessage()
msg['From'] = EMAIL_ADDRESS
msg['To'] = f'{receiver}'
msg['Subject'] = f'{site_code} - PowerClean - ShortcutQueries'
msg.set_content('Hello {contact}, \n Attached is the updated shortcut query. ')

# set up the SMTP server by using a contact manager
with smtplib.SMTP('localhost', 1027) as smtp:
    smtp.send_message(msg)

```

## Collect data from directory and store in a dataframe

We can use Python's os and sys libraries to move about our current working directory, to better retrieve the content for our emails. Create the logic, where we can hold the PII in order to quickly populate a dataframe.

## Run dataframe through a method that will send mass emails given arguments

#### Libraries
Import the smtplib module. It should be included in Python by default
