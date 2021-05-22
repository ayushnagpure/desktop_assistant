# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 07:59:40 2021

@author: Ayush Nagpure
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am Jarvis. Please tell me What can I do for you")
    
def takeCommand():
    #it will take microphone input from user and return String output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
        
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ayushnagpure62@gmail.com','xxxxxxxxxxx')
    server.sendmail('ayushnagpure27@gmail.com',to,content)
    server.close()
if __name__== "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipwdia...')
            query = query.replace("wikipwdia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = "C:\\Users\\Ayush\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
 
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
      
            
        elif 'email to ayush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ayushnagpure27@gmail.com"
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("sorry bro I am not able to send the email")
                
        elif 'quit' in query:
            speak("Thank YOU. I am always there for you")
            break
            
