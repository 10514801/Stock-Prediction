import datetime #The datetime module supplies classes for manipulating dates and times in both simple and complex ways
import pyttsx3 #pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
import os, sys #This module provides a portable way of using operating system dependent functionality.
import pandas as pd #It is use to Convert a Python’s list, dictionary or Numpy array to a Pandas data frame
#import yahoo_fin #Download historical stock prices, fundamentals data, income statements, cash flows, analyst info ,current cryptocurrency prices, and more with yahoo_fin.
#from yahoo_fin import stock_info as si 
import yfinance as yf
import speech_recognition as sr #Library for performing speech recognition, with support for several engines and APIs, online and offline

download_source= (r'/Users/saurabhwadhawane/stockdata1.csv')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)

while True:
     now = datetime.datetime.now()
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("Tell me, which market do you want to check?")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print('Done!')
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I did understand that. Please rerun the code')

            engine.runAndWait()
        else:
            engine.say("Please wait as I search and display the data for "+r.recognize_google(audio))
            engine.runAndWait() 
        userInput5 = (yf.download(r.recognize_google(audio))) 
        userInput6 = pd.DataFrame(data =userInput5) 
        print(userInput6)
        userInput6.to_csv(download_source)
        engine.runAndWait()
        break
        #, columns=['open','high','low','close','adjclose','volume','ticker']