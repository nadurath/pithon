import re
import os
from os import path
import time
import wave
import speech_recognition as sr
from datetime import datetime
import pywapi
import string
import cleverbot
import wikipedia
import pyaudio
import sys
from wordnik import *
from pygsr import Pygsr



#TEAM MEMBERS: Dawood Nadurath, Jordan Barnfield, Brennan Stuewe, Blake Ansley

#Written By Dawood Nadurath
#CS 1200.007

#Loop parameter to be replaced by GPIO input (switch on / off).

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
CHUNK = 512
RECORD_SECONDS = 5
WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "file.wav")

apiUrl = 'http://api.wordnik.com/v4'                            #API URL and Key to access wordnik api for dictionary function.
apiKey = '86de19100a8fdee3293060dab9601d980abf66f1bba238506'

client = swagger.ApiClient(apiKey, apiUrl)                                         #Initializing listener for audio from user.
b = cleverbot.Cleverbot()                                       #Initialize bot.
wordApi = WordApi.WordApi(client)

#p = pyaudio.PyAudio()

#stream = p.open(
#    format = FORMAT,
#    channels = CHANNELS, 
#    rate = RATE,
#    input = True,
#    frames_per_buffer = CHUNK)

#os.system('espeak "recording"')
#frames = []

#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#    data = stream.read(CHUNK)
#    frames.append(data)

#os.system('espeak "Finished recording!"')

#stream.stop_stream()
#stream.close()
#3p.terminate()

#waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#waveFile.setnchannels(CHANNELS)
#waveFile.setsampewidth(p.get_sample_size(FORMAT))
#waveFile.setframerate(RATE)
#waveFile.writeframes(b''.join(frames))
#waveFile.close()

r = sr.Recognizer()
with sr.WavFile(WAV_FILE) as source:
    audio = r.record(source)

req = r.recognize_google(audio)
print(req)
def tempSuggest():  # this function will suggest the type of clothes based on the temperature (written by Jordan Barnfield)
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
var1 = "\nIt is " + my_location['current_conditions']['text'].lower() + " and " + str(tempFah) + " degrees fahrenheit." + tempSuggest()
clearSkies = "Skies look clear today!"
chanceRain = int(my_location['forecasts'][1]['day']['chance_precip'])

#If statement that interprets user audio and outputs the function that corresponds to the user's request.
print "Working"
#Calls the weather function.
if "weather" in req or "forecast" in req or "temperature" in req:
    print var1
    cmd = "espeak {0}".format(var1)
    os.system('espeak "%s"' % var1)
    if(chanceRain is 0):
        print clearSkies
        os.system('espeak "%s"' % clearSkies)
    elif(chanceRain > 0):
        print chanceRain
        os.system('espeak "%s"' % chanceRain)
elif "define" in req or "find" in req or "fine" in req or "mean" in req or "definition" in req: #Calls the dictionary function.
    reqSplit = req.split()
    definitions = wordApi.getDefinitions(reqSplit[len(reqSplit)-1])
    os.system('espeak "%s"' % "Let me look that up for you.")
    os.system('espeak "%s"' % "The word" + reqSplit[len(reqSplit)-1] + "means")
    print definitions[0].text.split('.')[0]
    #os.system('espeak "%s"' % definitions[0].text.split('.')[0]) Won't work!
elif "Wiki" in req or "wikipedia" in req or "Google" in req:    #Calls the Wikipedia search function.
    os.system('espeak "%s"' % "Here's what Wikipedia returned!")
    os.system('espeak "%s"' % wikipedia.summary(req[5:]).split('.')[0])
elif "clever" in req or "clever bot" in req or "bot" in req:    #Calls the Cleverbot function.
    question = r.recognize_google(audio)
    reply = b.ask(question)
    os.system('espeak "%s"' % "Clever Bot says " + reply)
    print reply
elif "quit" in req or "shut down" in req or "enough" in req:    #Shuts the program down.
    os.system('espeak "%s"' % "Shutting down now.")