import requests

def joke():
    url = "https://joke3.p.rapidapi.com/v1/joke"

    querystring = {"nsfw":"false"}

    headers = {####
        }

    r = requests.request("GET", url, headers=headers, params=querystring)
    js=r.json()
    re=js['content']
    return (re)
