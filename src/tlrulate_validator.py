from src.tlrulate_request import *


#Permissible symbols (ASCI codes)
list = [95]
list += range(97, 123)
list += range(48, 58)

def valid_log(login, id):
    letter = True
    back_send = True
    for i in login:
        if ord(i.lower()) not in list: #Limiting the length of the name
            letter = False
    if len(login) < 2 or len(login) > 16 and letter:
        request_status_mess_6(id)
        back_send = False
    return back_send

#password validation
def valid_pass(login, id):
    back_send = True
    if len(login) < 5 or len(login) > 32:
        request_status_mess_7(id)
        back_send = False
    return back_send
