import cleverbot
import re

#TEAM MEMBERS: Dawood Nadurath, Jordan Barnfield, Brennan Stuewe, Blake Ansley

# Written by Jordan Barnfield
# CS1200.007


WORDS = []


def handle(text, mic, profile):
    mic.say("Ask me a question")

    b = cleverbot.Cleverbot() #initialize bot

    close = False #unused for loop

    while not close:
        question = mic.activelisten()
        if close(question): #if "exit" "quit" or "stop" is heard
            break #close loop
        reply = b.ask(question) #ask bot, get answer and store it in reply
        mic.say(reply)

def close(text):
    return bool(re.search(r"(exit|quit|stop)", text, re.IGNORECASE))

def isValid(text):
    return bool(re.search(r'\bot|question|cleverbot\b', text, re.IGNORECASE))




