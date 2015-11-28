import re
import wikipedia

#TEAM MEMBERS: Dawood Nadurath, Jordan Barnfield, Brennan Stuewe, Blake Ansley

#Written by Jordan Barnfield
#CS 1200.007

WORDS = ["WIKI", "WIKIPEDIA"] #keywords to detect

PRIORITY = 1

def handle(text, mic, profile):

        mic.say("What would you like me to search on Wikipedia?")

        def summary(text):
            mic.say(mic.say(wikipedia.summary(text))) #api function returns summary

        summary(mic.activeListen())


def isValid(text):
        return bool(re.search(r'\bwiki|wikipedia\b', text, re.IGNORECASE))



