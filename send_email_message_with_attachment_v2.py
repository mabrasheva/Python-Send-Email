# The script sends email message containing attachment.

import logging
import os
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def send_mail():
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as session:
            session.starttls()
            session.login(sender_email, password)
            session.sendmail(sender_email, receiver_email, message.as_string())
            session.quit()
    except (OSError, smtplib.SMTPException) as mail_err:
        print(f"Error occurred during email session: {mail_err}")
        logging.exception(f"Error occurred during email session: {mail_err}\n")


def date_and_time_format():
    now = datetime.now()
    date_and_time_string = now.strftime("%d %b %Y %H:%M:%S")
    return date_and_time_string


attachment_file_path = ""  # fill the attachment path. Example: "./Folder/file.csv"
sender_email = ""  # fill the sender email address
receiver_email = ""  # fill the receiver email address
password = ""  # fill the password
email_subject = "Python test mail message"
body_html = f"""\
    <html>
      <body>
        <p><strong>Report is completed.</strong><br>
        {date_and_time_format()}</p>
      </body>
    </html>
    """

attachment = MIMEBase('application', "octet-stream")
with open(attachment_file_path, 'rb') as file:  # Set file content as attachment payload
    attachment.set_payload(file.read())
encoders.encode_base64(attachment)  # Encode attachment file in base64
filename = os.path.basename(attachment_file_path)
attachment.add_header('Content-Disposition', f'attachment;filename = {filename}')

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = email_subject

message.attach(MIMEText(body_html, "html"))
message.attach(attachment)

send_mail()
