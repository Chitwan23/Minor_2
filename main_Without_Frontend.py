import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import whisper
import numpy as np
import requests
import webbrowser
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import cv2
import face_recognition

def face():
    known_image = face_recognition.load_image_file("me.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]
    match=False

    # Initialize the webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            # Check if the face matches with the known face
            match = face_recognition.compare_faces([known_encoding], face_encoding)
            name = "Unknown"    

            if match[0]:
                print("Match Found")
                # Release the webcam and close all OpenCV windows
                video_capture.release()
                cv2.destroyAllWindows()
                return True
                
            else:
                print("Not Match Found")

            # Draw a box around the face
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Label the face
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()    
    

genai.configure(api_key='')


def open_whatsapp():
    whatsapp_url = "https://web.whatsapp.com/"
    webbrowser.open(whatsapp_url)

def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("good morning!")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good evening!")

    speak("I am your personal assistant. Please tell me how can I help you")

def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def takecommand2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        # Save the audio data as an MP3 file
        with open("audio.mp3", "wb") as f:
            f.write(audio.get_wav_data())

    try:
        print("Recognizing...")
        model = whisper.load_model("base")
        transcript = model.transcribe("audio.mp3",fp16=False)
        query = transcript['text']
        print(f"User said: {query}\n")
    except Exception as e:
        print("Error:", e)
        print("Say that again please...")
        return "None"
    
    return query.lower() 



def takecommand():
     r = sr.Recognizer()
     with  sr.Microphone() as source: 
          print ("listening..") 
          r.pause_threshold = 1  
          audio=r.listen(source) 
     
     try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

     except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
     return query.lower()


def sendEmail(to, content):
    sender_email = 'singhchitwan08@gmail.com'
    sender_password = 'nkfd lyty clpn pphx'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to, content)
    server.close()




if __name__ == "__main__":
    if face():
        wishme()
        while True:
            if check_internet_connection():
                    print("Internet connection is available.")                
                    query = takecommand()
            else:
                print("No internet connection.")
                query = takecommand2()
            

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")
            
            elif 'open whatsapp' in query:
                open_whatsapp()

            elif 'open google' in query:
                webbrowser.open("https://www.google.com")

            elif 'play music' in query:
                music_dir = "C:\\Users\\yatha\\OneDrive\\Desktop\\Music"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\yatha\OneDrive\Desktop\Visual Studio Code.lnk"
                os.startfile(codePath)
                
            elif 'open Telegram' in query:
                codePath = "E:\Telegram Desktop\Telegram.exe"
                os.startfile(codePath)
            

            elif 'open word' in query:
                codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
                os.startfile(codePath)

            elif 'open Excel' in query:
                codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
                os.startfile(codePath)      

            elif 'exit' in query:
                speak("Exiting the program. Goodbye!")
                exit()

            elif 'send an email' in query:
                try:
                    speak("what should i say ?")
                    content = takecommand()
                    to = "yatharthsingh051@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")
            else:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(query)
                    cleaned_text = response.text.replace('*', '')
                    print(cleaned_text)
                    lines = cleaned_text.splitlines()
                    # Speak the first three lines
                    for i in range(min(5, len(lines))):
                        speak(lines[i])

