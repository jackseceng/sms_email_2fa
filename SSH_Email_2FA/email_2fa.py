import smtplib
import ssl
import random
import sys

def genkey():
    count = 0
    code = ""
    while count is not 4:
        newint = str(random.randint(0,9))
        code = code + newint
        count = count + 1
    return code

def input_is_correct(user_code, gend_code):
    if not user_code.isdigit():
        print('Codes contain only numbers.')
        return False
    elif len(user_code) is not 4:
        print('Codes are 4 digits long only.')
        return False
    elif user_code != gend_code:
        print('Code incorrect.')
        return False
    else:
        return True

def main(gend_code):
    user_code = str(input('Enter authentication code sent to your email address: '))
    attempt = 3
    check = input_is_correct(user_code, gend_code)
    while check is False:
        if attempt is 0:
            print('Out of attempts, a new code has been sent to your email address.')
            exit(1)
        user_code = input('Please try again, ' +str(attempt)+ ' trys remaining: ')
        check = input_is_correct(user_code, gend_code)
        attempt = attempt - 1
    if gend_code == user_code:
        print('Success, type "exit" to close conneciton.')
        exit(0)
    else:
        print('Unknown error, sorry.')
        exit(1)

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "<sender@gmail.com>"
receiver_email = "<receiver@domain.com>"
password = "<gmail-password>"
code = genkey()
message = """\
Subject: Authentication Code

Your code is: """ + code

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

main(code)
