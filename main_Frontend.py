import datetime
import tkinter as tk
from tkinter import ttk
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import face_recognition
import cv2
import google.generativeai as genai
from IPython.display import display
import requests

genai.configure(api_key='')

class AssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistant App")
        self.root.geometry("600x400")

        # Initialize Text-to-Speech Engine
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

        self.create_widgets()
        if self.authenticate_face():
            self.wish_me()
            self.voice_input()
        

    def create_widgets(self):
        self.input_label = ttk.Label(self.root, text="Enter your command:")
        self.input_label.pack(pady=10)

        self.input_entry = ttk.Entry(self.root, width=50)
        self.input_entry.pack()

        self.output_label = ttk.Label(self.root, text="Output:")
        self.output_label.pack(pady=10)

        self.output_text = tk.Text(self.root, width=60, height=10)
        self.output_text.pack()

        self.execute_button = ttk.Button(self.root, text="Execute", command=self.execute_command)
        self.execute_button.pack(pady=10)

        self.voice_button = ttk.Button(self.root, text="Voice Input", command=self.voice_input)
        self.voice_button.pack(pady=5)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        
    def wish_me(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.speak("Good morning!")
        elif 12 <= hour < 18:
            self.speak("Good afternoon")
        else:
            self.speak("Good evening!")

        self.speak("I am your personal assistant. Please tell me how can I help you")
        
    def authenticate_face(self):
        known_image = face_recognition.load_image_file("me.jpg") # Your image 
        self.known_encoding = face_recognition.face_encodings(known_image)[0]

        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()

            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for face_encoding in face_encodings:
                match = face_recognition.compare_faces([self.known_encoding], face_encoding)
                if match[0]:
                    self.speak("Face authenticated")
                    return True
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()

    def execute_command(self):
        command = self.input_entry.get()
        self.output_text.delete('1.0', tk.END)
        output = self.handle_command(command)
        self.output_text.insert(tk.END, output)
        
    def check_internet_connection():
        try:
            requests.get("http://www.google.com", timeout=3)
            return True
        except requests.ConnectionError:
            return False

    def voice_input(self):
        
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  
            audio = recognizer.listen(source)  

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, command)
            self.execute_command()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    def handle_command(self, command):
        if 'wikipedia' in command:
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            output = f"According to Wikipedia: {results}"
            self.speak(output)
            
        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            output = "Opening YouTube..."
            self.sp6eak(output)
            
        elif 'open whatsapp' in command:
            webbrowser.open("https://web.whatsapp.com/")
            output = "Opening WhatsApp..."
            self.speak(output)
            
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            output = "Opening Google..."
            self.speak(output)
            
        elif 'play music' in command:
            music_dir = "C:\\Users\\yatha\\OneDrive\\Desktop\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            output = "Playing music..."
            self.speak(output)
            
        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output = f"The time is {strTime}"
            self.speak(output)
            
        elif 'open code' in command:
            codePath = "C:\\Users\\yatha\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)
            output = "Opening Visual Studio Code..."
            self.speak(output)
            
        elif 'open telegram' in command:
            codePath = "E:\\Telegram Desktop\\Telegram.exe"
            os.startfile(codePath)
            output = "Opening Telegram..."
            self.speak(output)
            
        elif 'open word' in command:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(codePath)
            output = "Opening Microsoft Word..."
            self.speak(output)
            
        elif 'open excel' in command:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(codePath)
            output = "Opening Microsoft Excel..."
            self.speak(output)
            
        elif 'exit' in command:
            output = "Exiting the program. Goodbye!"
            self.speak(output)
            exit()
        elif 'send an email' in command:
            try:
                self.speak("What should I say?")
                content = self.takecommand()
                to = "yatharthsingh051@gmail.com"
                self.sendEmail(to, content)
                output = "Email has been sent!"
                self.speak(output)
            except Exception as e:
                output = f"Sorry, I am not able to send this email. Error: {str(e)}"
                self.speak(output)
        else:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(command)
            cleaned_text = response.text.replace('*', '')
            lines = cleaned_text.splitlines()
            output = "Here is the response:"
            for i in range(min(5, len(lines))):
                output += f"\n{lines[i]}"
            self.speak(output)
        return output

def main():
    root = tk.Tk()
    app = AssistantApp(root)
    
    root.mainloop()
    

if __name__ == "__main__":
    main()
