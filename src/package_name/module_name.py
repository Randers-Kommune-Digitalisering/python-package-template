import requests


def google_up():
    r = requests.get('https://google.com/')
    if r.ok:
        return True
    return False


def add(number1, number2):
    return number1 + number2
