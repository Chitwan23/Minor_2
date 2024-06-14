import os
import webbrowser
import datetime
import speech_recognition as sr
import openai

# Function to load the API key from a file
def load_api_key():
    try:
        with open('.Token', 'r') as file:
            return file.read().strip()  # Read the key and strip any extra whitespace
    except FileNotFoundError:
        print("API key file '.Token' not found.")
        exit()

# Global variables
chatStr = ""

# Set the API key from the file
openai.api_key = load_api_key()

def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Harry: {query}\nJarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def say(text):
    os.system(f'say "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Error:", e)
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I is activated")
    while True:
        print("Listening...")
        query = takeCommand()
        # Process the command based on query
        if "Jarvis Quit".lower() in query.lower():
            exit()

        # Add other conditions here
        else:
            print("Chatting...")
            chat(query)

# Add other features or functions as needed
