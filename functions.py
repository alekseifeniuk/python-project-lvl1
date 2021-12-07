import string
import secrets


def password():
    pass_temp = string.ascii_letters + string.digits
    passcode = ''.join(secrets.choice(pass_temp) for i in range(8))
    return passcode


def age_verification(age):
    while age <= 0:
        print('Age not correct. Try again!')
        age = int(input('Enter the age: '))
    return age


def is_marital(marital_status):
    if 'y' in marital_status.lower():
        return 'married'
    else:
        return 'not married'


def user_resume(name, age, marital_status):
    resume = 'My name is {}. Born {} years ago. I am {}.'.format(name, age, is_marital(marital_status))
    return resume
