import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to make the assistant speak
def speak(audiovoice):
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()

# Function to greet the user based on the time of the day
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 11:
        speak('Good Morning, Sir!')
    elif hour >= 11 and hour < 15:
        speak('Good Afternoon, Sir!')
    else:
        speak('Good Evening, Sir!')
    speak('I am your AI Assistant.')

# Function to ask for the user's name
def askname():
    speak('Can I know your good name, Sir?')
    name = takevoicecommand()
    speak('Welcome ' + name)
    speak('How can I help you, Sir?')

# Function to take voice commands from the user
def takevoicecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=30, phrase_time_limit=10)
            print("Processing your voice, please wait...")
            text = r.recognize_google(audio, language='en-in')
            print("You said:", text)
            return text.lower()
        except Exception:
            speak('Unable to recognize your voice. Can you repeat that?')
            return "None"

# Main function to execute voice commands
if __name__ == "__main__":
    greet()
    askname()

    while True:
        work = takevoicecommand()

        if 'how are you' in work:
            speak('I am fine, Thank you!')
            speak('How are you, Sir?')

        elif 'fine' in work or 'good' in work:
            speak('It is great to know that you are fine.')

        elif 'yes' in work or 'yeah' in work:
            speak('Wow, great job, Sir! All the best.')

        elif 'my faculty' in work or 'subject faculty' in work:
            speak('Your Subject Faculty is PC Karthik.')

        elif 'open project' in work:
            path = "C:\\Kalyan Reddy ( All Photos )\\AI Project"
            os.startfile(path)

        elif 'open my folder' in work:
            path = "C:\\Kalyan Reddy ( All Photos )"
            os.startfile(path)

        elif 'open chrome' in work:
            url = "https://techsrijan.com"
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)

        elif 'close chrome' in work:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'bye' in work:
            speak('Goodbye, Sir. Have a great day!')
            exit()

        else:
            speak("I didn't understand. Please repeat your command.")
