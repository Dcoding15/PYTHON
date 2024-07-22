from re import match
from typing import Union

def check_mail_syntax(input_mail: Union[ str |  None ] = None):
    ismail = match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', input_mail)
    if ismail is None:
        return False
    else:
        return True

def check_tel_syntax(input_tel: Union[ str | None ] = None):
    istel = match('^\+\s\d{1,3}\d{9,15}$', input_tel)
    if istel is None:
        return False
    else:
        return True

def check_passwd_syntax(input_passwd: Union[ str | None ] = None):
    ispasswd = match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W\_])[A-Za-z\d\W\_]{8,}$', input_passwd)
    if ispasswd is None:
        return False
    else:
        return True