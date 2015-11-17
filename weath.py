import re
from datetime import datetime
import pywapi
import string

class Weath:

    WORDS = []

    def rain(store):
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
        my_location = pywapi.get_weather_from_weather_com('75080')
        x = (int(my_location['current_conditions']['temperature']))
        string = ""
        if 0 > x:
            string = "It's freaking freezing! You need some warm clothes and a winter jacket. "
        elif (0 <= x) and (x < 5):
            string = "It's pretty cold out there. I'd suggest some warm clothes and possibly a jacket."
        elif (5 <= x) and (x < 16):
            string = "It's pretty chilly so I'd suggest some pants and a jacket. "
        elif (16 <= x) and (x < 22):
            string = "It's pretty solid outside today, some pants and a light sweater would feel great. "
        elif (22 <= x) and (x < 25):
            string = "It's a bit steamy today, shorts and a t shirt would feel great. "
        elif (25 <= x) and (x < 30):
            string = "It's hot today. I'd suggest wearing the minimal amount of clothes possible. "
        elif 30 <= x:
            string = "It's literally hell outside. I'd suggest going naked. "

        return string

    def handle(text, mic, profile):
        my_location = pywapi.get_weather_from_google('75080')
        location_status = my_location['current_conditions']['text']
        location_feelsliketemp = my_location['current_conditions']['feels_like']
        weather = "The weather conditions are " + location_status + " with a felt temperature of " + location_feelsliketemp + " degrees. "

        if ("clothes" in text.lower()) or ("wear" in text.lower()):

            chance_rain = rain(my_location['forecasts'])
            felttemp_int = int(location_feelsliketemp)
            weather_suggestion = tempSuggest(felttemp_int)

            weather_suggestion += chance_rain

            mic.say(weather_suggestion)

        elif ("hot" in text.lower()) or ("temperature" in text.lower()) or ("cold" in text.lower()):
            mic.say("It currently feels like " + location_feelsliketemp + " degrees.")
        elif "rain" in text.lower():
            rainyprop = rain(my_location['forecasts'])
            mic.say(rainyprop)

        else:
            mic.say(weather)


    def isValid(text):  # part of the jasper api documentation
        return bool(re.search(r'\b((rain|weather|wear|clothes|hot|cold|temperature))\b', text, re.IGNORECASE))

w = Weath()
#print w.tempSuggest()