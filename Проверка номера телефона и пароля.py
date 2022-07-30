def number_phone(number):
    length = len(number)
    int_number = number[0]
    return int_number == '+' and (length == 12)


print(number_phone(input('Введите номер телефона начиная с +7: ')))


def is_strong_password(password):
    LetterUpper, LetterLower, Digit = False, False, False
    for l in list(password):
        if l.istitle():
            LetterUpper = True
        if not l.istitle():
            LetterLower = True
        if l.isdigit():
            Digit = True
    if len(password) >= 12 and LetterUpper and LetterLower and Digit:
        return True
    else:
        return print('Пароль должен содержать символы нижнего и верхнего регистра.')


print(is_strong_password(input('Пароль должен содержать минимум 12 символов: ')))
