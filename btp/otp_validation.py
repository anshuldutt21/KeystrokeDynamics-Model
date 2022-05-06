# from email import message
import csv
import random as random
import smtplib

# function for otp generation
def generate_otp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(1,9))
    return otp

def fetch_user_email(username):
    filename = open('user_login_data.csv', 'r')
    file = csv.DictReader(filename)
    for row in file:
        if row['username'] == username:
            return row['email']

def check_otp_validation(username):
    otp = generate_otp()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("keystroke.model1@gmail.com", "buofeqfdmaflaiie")
    emailid = fetch_user_email(username)

    subject = 'OTP for Keystroke Dynamics based authentication model'
    body = "The one-time password for your login attempt is:\n" + otp
    email_text = 'Subject: {}\n\n{}'.format(subject, body)

    s.sendmail('&&&&&&&&&&&',emailid, email_text)
    s.quit()
    print("OTP sent successfully!")
    return otp
