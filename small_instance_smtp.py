# import the smtplib module. It should be included in Python by default
import smtplib
from email.message import EmailMessage

from decouple import config


def main():
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
    msg.set_content('Hello , \n Attached is the updated shortcut query for the MDS Excel Add in. Please note that '
                    'this updated query is needed to ensure that you are loading the newest MDS columns')
    # set up the SMTP server by using a contact manager
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    with smtplib.SMTP('localhost', 1028) as smtp:
        #     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #     smtp.sendmail(EMAIL_ADDRESS, 'ggian205@aol.com', msg)
        smtp.send_message(msg)
