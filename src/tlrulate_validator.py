#статусы ошибок
request_status = {
1 : "all ok",
2 : "Упс. Что-то случилось с сайтом. Попробуем достучатся до него позднее. А пока, можешь написать о проблеме разрабу /write ",
3 : "В  последднее время на этот акаунт пытались зайти слишком много раз. Включилась блокировка. Придётся подождать пока она не снимется. А пока, можешь написать о проблеме разрабу /write",
4 : "Неправильно указан логин или пароль.",
5 : "Что-то с парсером не так.",
6 : "Такого логина быть не может. Попробуй ввести логин ещё раз",
7 : "Такого пароля быть не может. Попробуй ввести пароль ещё раз",
8 : "Запрос от селениума к бд на обновление данных",
9 : "Неполадки с ботом, обратить в поддержку" # something with the database
}



#Login's validation
list = []
list += range(97, 123) #Permissible symbols (ASCI codes)
list += range(48, 58)
list.append(95)

def valid_log(login):
    for i in login:
        n = ord(i.lower())
        if n in list: #Limiting the length of the name
            letter = True
        else:
            letter = False
    if len(login) >= 2 and len(login) <= 16 and letter:
        back_send = request_status[1]
    else:
        back_send = request_status[6]
    return back_send

#password validation
def valid_pas(login):
    if len(login) >= 5 and len(login) <= 32:
        back_send = request_status[1]
    else:
        back_send = request_status[7]
    return back_send
