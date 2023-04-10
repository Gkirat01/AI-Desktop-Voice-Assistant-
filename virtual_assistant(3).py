

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
import smtplib
from requests import get


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello I Am Ironman.Please tell me how may i help you")


def takeCommand():
    #It takes microphone inputs from user andf returns string output
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2, phrase_time_limit=5)

     try:
         print("Recognize...")
         query = r.recognize_google(audio, language='en-in')
         print(f"user said: {query}\n")

     except Exception as e:
         #print(e)

        print("say that again please...")
        return "None"
     return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('paulrobertttz@gmail.com', 'robert_123')
    server.sendmail('paulrobertttz@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()

    while True:
      query = takeCommand().lower()
      if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=1)
          speak("According to Wikipedia")
          print(results)
          speak(results)
      elif 'open youtube' in query:
          speak("sir, what should i search on youtube")
          b = takeCommand().lower()
          webbrowser.open(f"{b}")


      elif 'open google' in query:
          speak("sir, what should i search on google")
          a = takeCommand().lower()
          webbrowser.open(f"{a}")

      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")

      elif 'play music' in query:
          music_dir = 'C:\\Users\\intel\\Music\\music'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[0]))

      elif "ip address" in query:
          ip = get('https://api.ipify.org').text
          speak(f"your ip address is{ip}")

      elif "open notepad" in query:
          npath = "C:\\Windows\\system32\\notepad.exe"
          os.startfile(npath)

      elif 'the time ' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"sir, the time is {strTime}")

      elif 'open camera' in query:
          cap = cv2.VideoCapture(0)
          while True:
              ret,  img = cap.read()
              cv2.imshow('webcam', img)
              k = cv2.waitKey(50)
              if k==27:
                  break;
          cap.release()
          cv2.destroyAllWindows()

      elif "email to robert" in query:
          try:
              speak("what should i say to robert")
              content = takeCommand().lower()
              to = "paulrobertttz@gmail.com"
              sendEmail(to, content)
              speak("Email has been sent")

          except Exception as e:
              print(e)
              speak("sorry bro, i am not able to send the email")

      elif "ok thanks" in query:
          speak(" anytime sir.thanks for using me, have a nice day")










