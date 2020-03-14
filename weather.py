import requests
def weather(zip):
    url = "https://us-weather-by-zip-code.p.rapidapi.com/getweatherzipcode"

    querystring = {"zip":zip}

    headers = {####
        }

    r = requests.request("GET", url, headers=headers, params=querystring)
    js=r.json()
    #Sorting result
    result=("City:"+js["City"]+"\nState:"+js["State"]+"\nTempF:"+js["TempF"]+"\nTempC:"+js["TempC"]+"\nWeather:"+
            js["Weather"]+"\nWindMPH:"+js["WindMPH"]+"\nWindDir"+js["WindDir"]+"\RelativeHumidity:"+
            js["RelativeHumidity"]+"\nVisibilityMiles:"+js["VisibilityMiles"])
    return result
