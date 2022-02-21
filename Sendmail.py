

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_id = 'Senders mail id'
    to_id = 'Client mail id'
    subject = "Finance Report"

    msg = MIMEMultipart()
    msg['From'] = from_id
    msg['To'] = to_id
    msg['Subject'] = subject

    body = "<b>Today's Stock Market Report</b>"
    msg.attach(MIMEText( body , 'html'))

    my_file  = open(filename, 'rb') 

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)

    message = msg.as_string()


    server = smtplib.SMTP('smtp.gmail.com' , 587)
    #encription to make server strong
    server.starttls()
    server.login(from_id , 'moggbatljwjwziop')

    server.sendmail(from_id, to_id , message)

    server.quit()