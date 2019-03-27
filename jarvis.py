from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser


def speak(audio):
    # speak
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


# listens for commands
def getcommand():
    # record command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + "\n")

    # loop back to continue if not recognized
    except sr.UnknownValueError:
        command = ''

    return command


# if statements for executing commands
def assistant(command):
    # Commands
    if 'open Reddit' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = 'https://www.reddit.com'
        webbrowser.get(chrome_path).open(url)

    if 'open Google' in command:
        os.system('google-chrome')

    if 'open Spotify' in command:
        os.system('spotify')

    if 'open whatsapp' in command:
        os.system('whatsdesk')

    if 'open pycharm' in command:
        os.system('pycharm')

    if 'open idea' in command:
        os.system('intellij')

    if 'open Discord' in command:
        os.system('discord')

    if 'open translate' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = 'https://translate.google.com/'
        webbrowser.get(chrome_path).open(url)

    if 'open stackoverflow' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = 'https://stackoverflow.com/'
        webbrowser.get(chrome_path).open(url)

    if 'open mail' in command:
        os.system('mailspring')

    if 'what\'s up' in command:
        speak('Not much')
        speak('Not much just chilling, Bruv')

    if 'open Spotify' in command:
        os.system('spotify')


# endless loop
while True:
    speak("I am ready for your next command: ")
    assistant(getcommand())
