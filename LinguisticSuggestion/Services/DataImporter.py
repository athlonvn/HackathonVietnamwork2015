# Import data from Vietnamwork API and pythonize it
import requests
import json

HOST = "https://api-staging.vietnamworks.com"
LOGIN_URL = HOST + "/users/login"
SEARCH_URL = HOST + "/jobs/search"
DEFAULT_KEY = "6ff124a0f3ec81aa89eaa534f856fcac6761f6366f619a2e0dc2150485ea829d"
USER_NAME = "athlonvn@gmail.com"
PASSWORD = "123456"


def LoginVietnamWork():
    token = ""
    response = requests.post(LOGIN_URL ,
                    data = json.dumps({"user_email" : USER_NAME, "user_password" : PASSWORD}),
                    headers = {"CONTENT-MD5":DEFAULT_KEY, "Content-Type":"application/json"})
    if response.status_code != 200:
        return None
    try:
        response_data = json.load(str(response.text))
        token = response_data['data']['profile']['login_token']
    except Exception as ex:
        print str(ex)
        return None
    return token


def GetSearchDataVietnamWork():
    response = requests.post(SEARCH_URL,headers = {"CONTENT-MD5":DEFAULT_KEY})
    data = json.loads(response.text)
    return data


print GetSearchDataVietnamWork()