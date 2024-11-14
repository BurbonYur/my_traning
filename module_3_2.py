def check_adr(adress):
    zone_ = ".com", ".ru", ".net"
    inv_zone = 0
    for i in zone_:
        if adress.find(i, (len(adress) - len(i))) == -1:
            inv_zone += 1
        else:
            break
    if inv_zone == len(zone_):
        return False
    else:
        return True


def send_email(message, recipient, sender='university.help@gmail.com'):
    if sender.find("@") == -1 or recipient.find("@") == -1:
        return "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient + "."
    if check_adr(recipient) == False or check_adr(sender) == False:
        return "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient + "."
    if recipient == sender:
        return "Нельзя отправить письмо самому себе!"
    if sender == "university.help@gmail.com":
        return "Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient + "."
    else:
        return "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient + "."


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
