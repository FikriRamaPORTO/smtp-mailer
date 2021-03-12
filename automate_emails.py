import os
import smtplib
from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

import pandas as pd
from decouple import config

# Get environment details
EMAIL_ADDRESS = config('EMAIL_USER')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')
# print(EMAIL_ADDRESS)
# print(EMAIL_PASSWORD)

# print(os.listdir())
# os.chdir("Queries")
# os.chdir("../")
os.chdir("C:/Users/ggian/Desktop/Untitled Folder")

# get data from excel
df_Site_Code = pd.read_excel('ContactInfo.xlsx', engine='openpyxl', sheet_name='Contacts')['SITE_CODE']
df_CBS_CONTACT = pd.read_excel('ContactInfo.xlsx', engine='openpyxl', sheet_name='Contacts')['CBS_CONTACT']
df_EMAIL = pd.read_excel('ContactInfo.xlsx', engine='openpyxl', sheet_name='Contacts')['EMAIL']


def create_metadata(contact, receiver, site_code, file):
    # Create the email message
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = f'{receiver}'
    msg['Subject'] = f'{site_code} - PowerClean - ShortcutQueries'
    msg.set_content(
        f'Hello {contact}, Attached is the updated shortcut query for the MDS Excel Add in. Please note that this '
        'updated query is needed to ensure that you are loading the newest MDS columns')
    print('TO: ', f'{receiver}')
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.send_message(msg)
        #     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        #     smtp.sendmail(EMAIL_ADDRESS, 'ggian205@aol.com', msg)


# set up the SMTP server by using a contact manager
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# with smtplib.SMTP('localhost', 1027) as smtp:

def create_ssl(contact, receiver, site_code, file):
    # Create the email message
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = f'{receiver}'
    msg['Subject'] = f'{site_code} - PowerClean - ShortcutQueries'
    msg.set_content(
        f'Hello {contact}, \n\nAttached is the updated shortcut query for the MDS Excel Add in. Please note that this '
        'updated query is needed to ensure that you are loading the newest MDS columns.'
        'I would also like to take the opportunity to encourage you to begin massaging the data that is now loaded '
        'onto MDS. '
    )

    print('TO: ', f'{receiver}')

    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # smtp.send_message(msg)
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        # smtp.sendmail(EMAIL_ADDRESS, 'ggian205@aol.com', msg)


absolute_path = r"C:\Users\ggian\Desktop\Untitled Folder\Queries"

for index in range(len(df_Site_Code)):
    # start sending the emails
    contact = df_CBS_CONTACT[index]
    receiver = df_EMAIL[index]
    site_code = df_Site_Code[index]

    print(df_CBS_CONTACT[index])

    # print("I am in the correct query!")
    files = os.listdir(absolute_path)
    # print("Now inside Queries Directory", os.getcwd())
    os.chdir(absolute_path)
    file = site_code + ".txt"

    create_metadata(contact, receiver, site_code, file)

    if index == 9:
        create_ssl(contact, receiver, site_code, file)

print("Grabbed all the files, let's book it! Restoring the path")
os.chdir("../")
