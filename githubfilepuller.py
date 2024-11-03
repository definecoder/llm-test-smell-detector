import requests

from dotenv import load_dotenv  
import os

load_dotenv('.env.local')
PERSONAL_ACCESS_TOKEN = os.getenv('PERSONAL_ACCESS_TOKEN')

def get_file_url(owner, name, search_term, branch):
    try:
        url = f"https://github.com/search/suggestions?query=repo%3A{owner}%2F{name}+{search_term}&saved_searches=%5B%5D"
        headers = {
            "Accept": "application/json",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cookie": "_device_id=8e3d4ff2172350ecbc9c250d45c86c4d; user_session=GBvLbTY6yuxDrRPt2fz5Z4Fqco-LMnIN-MpLoyhAIk-l_9fZ; __Host-user_session_same_site=GBvLbTY6yuxDrRPt2fz5Z4Fqco-LMnIN-MpLoyhAIk-l_9fZ; logged_in=yes; dotcom_user=shawon-majid; _octo=GH1.1.1021282052.1727531594; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=dark; tz=Asia%2FDhaka; _gh_sess=glQssnyj26bVvX%2FaMTr9qA4KnadknGFYJzyCHi6iTy0yG6O%2BnAPqrTt0waqn3y3P%2F28RTHJP5aSYr7Xs33dXhggwR9gYFXOUNG5BZdzZLK8QEhQB9PcavUjJbq3n9GEIbnktkl6WLVb2UWrFS9fMgQCWaVj3wXTZTPMB5srQVyKU%2FBk6pWOc9RPjQJ4UM5zOT72ZDxole%2FqY3N1%2BaAL4e2%2FaVg%2FKptGKeSbMAELmW97Q7Lua15mDd8xKVZmaYqaogh2cNPKDW%2BmQJ6IoM%2FUkbrbntUeast6Zcx2lUaXvvi7OYIfYHUrWLw5mEC%2FcnbbN6NiMuQMEajt1TzXAolI7D4wUREK6GYBh%2FrRx1whGu6B4Q5YVV%2BYBSW7Gen4E28V%2B--sI9bLXjqqtKLURoi--RcTqVXzDKU%2FhEp4rWaZWSA%3D%3D",
            "Authorization": f"Bearer {PERSONAL_ACCESS_TOKEN}"
        }

        response = requests.get(url, headers=headers)

        data = response.json()
        destination_url = f"https://github.com/{owner}/{name}/blob/{branch}/{data['suggestions'][0]['path']}"
        return destination_url
    except Exception as e:
        print(e)



