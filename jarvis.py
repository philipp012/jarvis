from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


# listens for commands
def command():
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
        assistant(command())

    return command


# if statements for executing commands
def assistant(command):
    if 'open Reddit' in command:
        chrome_path = '/user/bin/google-chrome'
        url = 'https://www.reddit.com'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Not much just chilling, Bruv')
        
    if 'open Spotify' in command:
        os.open('/user/bin/spotify')


talkToMe("I am ready for your Command")

while True:
    assistant(command())
