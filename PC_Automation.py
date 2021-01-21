import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import operator
import json
import wolframalpha
import time
from urllib.request import urlopen
import requests

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #12 hours clock
    speak("The Current time is ")
    speak(Time)

#time_()

def date_():
    today =  datetime.date.today().strftime('%d %B, %Y')
    
    speak("The current date is ")
    speak(today)

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/hp/Pictures/Screenshots")

def wishme():
    speak("Welcome Vikas!")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if(hour>=6 and hour<12):
        speak("Good Morning!")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon!")
    elif(hour>=18 and hour<24):
        speak("Good Evening!")
    else:
        speak("It's time to take rest!")

    speak("At your service Sir! Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please.....")
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    
    server.login('username','password')
    server.sendmail('username',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    speak('percent')

    battery = psutil.sensors_battery()
    speak('Battery is at ')
    speak(battery.percent)
    speak('percent')

def jokes():
    speak('pyjokes.get_joke')

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()

    wishme()

    while True:
        query = TakeCommand().lower()

        if "time" in query:
            time_()
        elif "date" in query:
            date_()
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=3)
            speak('according to wikipedia')
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should I say?")
                content = TakeCommand()
                speak('who is the receiver?')
                receiver = input("Enter receiver email address here: ")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')
            except Exception as e:
                print(e)
                speak('Unable to send email.')
        elif 'search' in query: 
            query = query.replace("query","")
            wb.open(query)
        elif 'youtube' in query:
            speak('what should i show you from youtube?')
            search_term = TakeCommand().lower()
            speak('Here we go!')
            wb.open('https://www.youtube.com/results?search_query='+search_term)
        elif 'google' in query:
            speak('what should i show you on Google?')
            search_term = TakeCommand().lower()
            speak('Here we go!')
            wb.open('https://www.google.com/search_q='+search_term)
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'go offline' in query:
            speak('Going offline Sir!')
            quit()
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Emptied.")
        elif 'write a note' in query:
            speak('What should i write?')
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak('Should I include date and time?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes.')
            else:
                file.write(notes)
                speak('Done taking notes.')
        elif "show note" in query:
            speak("Showing Notes")
            file = open("notes.txt", "r")
            print(file.read())
            speak(file.read())
        elif 'take screenshot' in query:
            screenshot()
            speak("Done!") 
         elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")  
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

            