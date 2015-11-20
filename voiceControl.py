import re
import speech_recognition as sr
from datetime import datetime
import pywapi
import string
import pyttsx
from wordnik import *

while True:

    apiUrl = 'http://api.wordnik.com/v4'
    apiKey = 'MY_API_KEY'
    client = swagger.ApiClient(apiKey, apiUrl)
    r = sr.Recognizer()
    wordApi = WordApi.WordApi(client)
    
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        engine.say("How can I help you?")
        engine.runAndWait()
        audio = r.listen(source)

    req = r.recognize_google(audio)
    def tempSuggest():  # this function will suggest the type of clothes based on the temperature
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

    my_location = pywapi.get_weather_from_weather_com('75080')
    tempFah = int(int(my_location['current_conditions']['temperature'])*1.8 + 32)

    if "weather" in req or "forecast" in req or "temperature" in req:
        engine.say("\nIt is " + my_location['current_conditions']['text'].lower() + " and " + str(tempFah) + " degrees fahrenheit.")
        engine.say(tempSuggest())
        engine.runAndWait()
        chanceRain = int(my_location['forecasts'][1]['day']['chance_precip'])
        if(chanceRain is 0):
            engine.say("Skies look clear today!")
            engine.runAndWait()
        elif(chanceRain > 0):
            engine.say("There's a " + str(chanceRain) + "percent chance of rain today. Plan accordingly.")
            engine.runAndWait()
    elif "define" in req or "find" in req or "fine" in req or "mean" in req or "definition" in req:
        reqSplit = req.split()
        definitions = wordApi.getDefinitions(reqSplit[len(reqSplit)-1])
        engine.say("Let me look that up for you.")
        engine.say("The word" + reqSplit[len(reqSplit)-1] + "means" + definitions[0].text)
        engine.runAndWait()
    elif "music" in req or "play" in req or "tunes" in req or "song" in req:
        engine.say("Coming right up!")
        engine.runAndWait()
    elif "quit" in req or "shut down" in req or "enough" in req:
        engine.say("Shutting down now.")
        engine.runAndWait()
        break
