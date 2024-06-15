# Minor_2

**AI ASSISTANT FOR DESKTOP**

Welcome to the AI Assistant project! This repository contains the code for a personal AI assistant capable of performing various tasks such as recognizing faces, taking voice commands, searching Wikipedia, opening websites, playing music, checking internet connection, and sending emails. This assistant uses several Python libraries and APIs to provide these functionalities.

**Features**

Face Recognition: Identifies the user via webcam before proceeding with tasks.

Voice Commands: Takes voice commands from the user to perform actions.

Wikipedia Search: Retrieves and reads out summaries from Wikipedia.

Open Websites: Opens popular websites like YouTube, Google, WhatsApp, etc.

Play Music: Plays music from a specified directory.

Check Time: Tells the current time.

Open Applications: Opens applications like Visual Studio Code, Word, Excel, Telegram.

Send Emails: Sends emails using Gmail SMTP.

Check Internet Connection: Checks for active internet connection.

**Installation**

To run this project, you need to have Python installed on your system along with the following libraries:

**pyttsx3
speech_recognition
wikipedia
webbrowser
os
smtplib
whisper
numpy
requests
google.generativeai
opencv-python
face_recognition**

**You can install these dependencies using pip:**

pip install pyttsx3 SpeechRecognition wikipedia requests opencv-python face_recognition numpy whisper google-generativeai

**Usage**

**Face Recognition:**

Ensure you have a reference image named me.jpg in the working directory.
The assistant will activate upon recognizing the face.

**Voice Commands:**

The assistant will greet you based on the time of the day.
Speak your command clearly into the microphone.

**Commands:**

**Wikipedia Search:** Say "Wikipedia [topic]".

**Open Websites:** Say "open YouTube", "open Google", "open WhatsApp".

**Play Music:** Say "play music".

**Check Time:** Say "the time".

**Open Applications:** Say "open code", "open word", "open excel", "open Telegram".

**Send Emails:** Say "send an email".

**Exit:**
To exit the program, say "exit".

**Code Overview**

**Face Recognition**
The face() function uses OpenCV and the face_recognition library to detect and match faces using the webcam.

**Voice Commands**
The takecommand() and takecommand2() functions use the speech_recognition and whisper libraries to process voice commands.

**Sending Emails**
The sendEmail() function uses the smtplib library to send emails via Gmail's SMTP server.

**Main Functionality**
The wishme() function greets the user. Based on the commands received, various actions are performed such as searching Wikipedia, opening websites, playing music, checking the time, opening applications, and sending emails.

**Contribution**

Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue to discuss what you would like to change
