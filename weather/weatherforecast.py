# !/usr/bin/python
import sys
import mailer
import weather

def get_emails():

    # Reading emails from a file
    emails = {}
    
    try:
    	email_file = open('emails.txt', 'r')

    	for line in email_file:
    	    (email, name) = line.split(',')
            emails[email] = name.strip()
    except IOError as err:
    	print err
    
    return emails

def main():
    # Get our dictionary of customer emails and names
    emails = get_emails()
    forecast=weather.get_weather_forecast()
    mailer.send_emails(emails,forecast)

main()

