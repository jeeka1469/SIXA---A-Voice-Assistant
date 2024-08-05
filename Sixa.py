import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Hey' in command:
                command = command.replace('Hey', '')
                print(command)
    except:
        pass
    return command

def run_sixa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who' in command or 'what' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'How are you' in command:
        talk('I am Good You Say')
    elif 'bored' in command:
        talk('Go And Study')
    elif 'open' in command:
        if 'open browser' in command:
            talk('opening Browser')
            os.system('start chrome.exe')
        elif 'open calculator' in command:
            talk('opening calculator')
            os.system('calc.exe')
        elif 'open notepad' in command:
            talk('opening notepad')
            os.system('notepad.exe')
        elif 'open Task Manager' in command:
            talk('opening task manager')
            os.system('taskmgr.exe')
        elif 'open spotify' in command:
            talk('opening spotify')
            os.system('spotify.exe')
        elif 'open settings' in command:
            talk('opening settings')
            os.system('settings')
        elif 'open file manager' in command:
            talk('opening file manager')
            os.system('explorer.exe')

    else:
        talk('Please say the command again.')

    
while True:
    run_sixa()
