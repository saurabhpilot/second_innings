# /usr/bin/python

import smtplib
import socket
import sys

def send_emails(emails,forecast):

    # Connect to smtp server and tls encryption
    try:
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.starttls()
    except smtplib.SMTPAuthenticationError as err:
        print err
        sys.exit()
    except socket.gaierror as err:
    	print err
    	sys.exit()
    except socket.error as err:
    	print err
    	sys.exit()

    # Login

    password = raw_input("what's your password?")
    from_email='nexus69629@gmail.com'
    server.login(from_email, password)
    for to_email, name in emails.items():
        message='Subject: Hello from Saurabh\n'
        message+='Hi ' + name + '!\n\n'
        message+=forecast
        server.sendmail(from_email, to_email,message)
    server.quit()

