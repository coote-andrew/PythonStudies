#Is American phone number
import re


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8-12):
        if not text[i].isdecimal():
            return False
    return True



print(isPhoneNumber('415-565-1242'))

def findPhoneNumber(message):
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')

message = 'Cal me at 415-555-0909 tomorrow. 514-888-9999 is my office.'

findPhoneNumber(message)


def findPhoneNumberV2(text):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search(text)
    print('Phone number found: ' + mo.group())


findPhoneNumberV2(message)

    


