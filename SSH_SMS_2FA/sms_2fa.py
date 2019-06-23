import urllib.request
import urllib.parse
import random
import sys

def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

def genkey():
    count = 0
    code = ""
    while count is not 4:
        newint = str(random.randint(0,9))
        code = code + newint
        count = count + 1
    return code

def gen_and_send():
    code = genkey()
    resp =  sendSMS('<textlocal-api-key>', '<recipient-number>',
        '<sender-name>', code)
#    print(resp) #Both of these print statements are for debugging and must be commented out by default
#    print(code)
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

def main():
    gend_code = str(gen_and_send())
    user_code = str(input('Enter authentication code sent to your mobile number: '))
    attempt = 3
    check = input_is_correct(user_code, gend_code)
    while check is False:
        if attempt is 0:
            print('Out of attempts, a new code has been sent to your mobile number.')
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

if __name__ == "__main__":
    main()
