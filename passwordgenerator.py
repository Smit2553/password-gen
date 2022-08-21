import string
import random


def generate_random_password(options, number: int):
    capitalletters = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    digits = list(string.digits)
    special_characters = list("!@#$%^&*()")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    password = []
    if len(options) != 0:
        letterrange = number / len(options)
    elif len(options) == 0:
        letterrange = int(number) / int(4)
    else:
        letterrange = 4
    letterrange = int(letterrange)
    if 'upper' in options:
        for i in range(letterrange):
            password.append(random.choice(capitalletters))
    if 'lower' in options:
        for i in range(letterrange):
            password.append(random.choice(lowercase))
    if 'num' in options:
        for i in range(letterrange):
            password.append(random.choice(digits))
    if 'char' in options:
        for i in range(letterrange):
            password.append(random.choice(special_characters))
    if len(password) < number:
        for i in range(number - len(password)):
            if 'upper' in options:
                password.append(random.choice(capitalletters))
            elif 'lower' in options:
                password.append(random.choice(lowercase))
            elif 'num' in options:
                password.append(random.choice(digits))
            elif 'char' in options:
                password.append(random.choice(special_characters))
            else:
                password.append(random.choice(characters))
    random.shuffle(password)
    return password
