import requests


def call_api():

    url= 'https://api.github.com/users'
    response = requests.get(url)
