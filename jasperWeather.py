import re
from datetime import datetime
import pywapi

#TEAM MEMBERS: Dawood Nadurath, Jordan Barnfield, Brennan Stuewe, Blake Ansley

#Written by Jordan Barnfield
#CS1200.007

WORDS = [] #key words to look for, left empty b/c defined below in isValid

def rain(store): #function to determine chance of rain
    date = datetime.now().day
    integer = 0
    location = 0
    hold = ""

    for day in store:
        if str(date) in day["date"].lower():
            location = integer

        integer += 1

    chance_string = store[location]["day"]["chance_precip"]
    chance = int(chance_string)
    #based on % chance
    if (0 <= chance) and (chance <= 30):
        hold += "It should not rain , so don't bother taking an umbrella with you."
    elif (30 < chance) and (chance <= 50):
        hold += "There's a slight chance of rain today, it's a good idea to have an umbrella on you. "
    elif (50 < chance) and (chance < 65):
        hold += "There's a good chance of rain today, make sure to keep an umbrella on you."
    else:
        hold += "Keep in mind though that it's definitely going to rain today, so do take an umbrella."

    return hold


def tempSuggest(temp):  # this function will suggest the type of clothes based on the temperature
    global string
    string = ""
    #based on temperature
    if 32 > temp:
        string = "It's freaking freezing! You need some warm clothes and a winter jacket. "
    elif (32 <= temp) and (temp < 5):
        string = "It's pretty cold out there. I'd suggest some warm clothes and possibly a jacket."
    elif (41 <= temp) and (temp < 16):
        string = "It's pretty chilly so I'd suggest some pants and a light jacket. "
    elif (60 <= temp) and (temp < 22):
        string = "It's pretty solid outside today, some pants and a t shirt would feel great. "
    elif (71 <= temp) and (temp < 25):
        string = "It's a bit steamy today, shorts and a t shirt would feel great. "
    elif (77 <= temp) and (temp < 30):
        string = "It's hot today. I'd suggest wearing the minimal amount of clothes possible. "
    elif 86 <= temp:
        string = "It's literally hell outside. I'd suggest going naked. "

    string += ". "
    return string


def handle(text, mic, profile):
    my_location = pywapi.get_weather_from_weather_com('USTX1134') #api usage to get richardson data
    location_status = my_location['current_conditions']['text'] #api call to get location data
    location_feelsliketemp = my_location['current_conditions']['feels_like'] #api call to get felt temp
    weather = "The weather conditions are " + location_status + " with a felt temperature of " + location_feelsliketemp + " degrees. " #use api call to put in string

    if ("clothes" in text.lower()) or ("wear" in text.lower()): #get spefiic data from request

        chance_rain = rain(my_location['forecasts']) #get rain info
        felttemp_int = int(location_feelsliketemp) #get felttemp info
        weather_suggestion = tempSuggest(felttemp_int) #function call with given information

        weather_suggestion += chance_rain #concatanate strings

        mic.say(weather_suggestion)

    elif ("hot" in text.lower()) or ("temperature" in text.lower()) or ("cold" in text.lower()): #get specific data from request
        mic.say("It currently feels like " + location_feelsliketemp + " degrees.")
    elif "rain" in text.lower():
        rainyprop = rain(my_location['forecasts'])
        mic.say(rainyprop)

    else:
        mic.say(weather)


def isValid(text):  # part of the jasper api documentation
    return bool(re.search(r'\b((rain|weather|wear|clothes|hot|cold|temperature))\b', text, re.IGNORECASE))
