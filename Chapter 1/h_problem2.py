
# Anything that we type will be pronounced 

import pyttsx3
engine = pyttsx3.init()

engine.say('''
pyttsx3 is a Python library that turns text into speech. It works offline, lets you adjust voice, speed, and volume, and runs on Windows, macOS, and Linux — perfect for adding voice to your Python project''')

engine.runAndWait()

