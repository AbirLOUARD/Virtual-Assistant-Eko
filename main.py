import sys
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime
import wikipedia
import random
import webbrowser

#Reconnaître la parole
listner = sr.Recognizer()
#Initialiser la voix
engine = ttx.init()
#Fixer les paramètres
voice1 = engine.getProperty('voices')
#Si vous voulez la voix féminine utilisez "voice1[3].id"
engine.setProperty('voice', 'french')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Parlez maintenant ")
            voice = listner.listen(source)
            command = listner.recognize_google(voice, language='fr-FR')
            command.lower()
    except:
        pass
    return command

def the_assistant():
    command = listen()
    print(command)
    name = "eko"
    user = "abir"
    hour = datetime.datetime.now().hour
    if ("bonjour" in command) or ("salut" in command) or ("bonsoir" in command):
        if hour > 6:
           text = ('Bonjour {}'.format(user))
           talk(text)
        elif hour > 19:
            text = ("Bonsoir {}".format(user))
            talk(text)
        elif (hour == 21, 22, 23) and (hour < 5):
            text = ("je pense que c'est le moment pour dormir {}".format(user))
            talk(text)
    elif "écho" in command:
        text = "Comment puis-je vous aider?"
        talk(text)
    elif "ça va" in command:
        text = "oui et vous?"
        talk(text)
    elif "et toi" in command:
        text = ["super merci", "je vais bien"]
        talk(random.choice(text))
    elif ("oui" in command) or ("oui merci" in command):
        text = "d'accord super"
        talk(text)
    elif ("ton nom" in command) or ("comment tu t'appelles" in command):
        text = ("je m'appelle {}".format(name))
        talk(text)
    elif "inventé" in command:
        text = "c'est abir louard qui m'a crée"
        talk(text)
    elif "chanson " in command:
        chanteur = command.replace("chanson ", '')
        talk("chanson en cours")
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif "heure" in command:
        heure = datetime.datetime.now().strftime('%H:%M:%S')
        talk("il est" + heure)
    elif "qui est" in command:
        person = command.replace("qui est", '')
        wikipedia.set_lang("fr")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif ("cherche-moi" in command) or ("cherche" in command):
        recherche = command.replace("cherche-moi", '')
        recherche = pywhatkit.search(recherche)
        text = "c'est-ce que j'ai pu trouver"
        talk(text)
    elif "ouvre Gmail" in command:
        webbrowser.open_new("https://mail.google.com/")
        talk("Gmail s'ouvre dès maintenant")
    elif "ouvre github" in command:
        webbrowser.open_new("https://github.com/")
        talk("github s'ouvre dès maintenant")
    elif "ouvre YouTube" in command:
        webbrowser.open_new("https://www.youtube.com/")
        talk("github s'ouvre dès maintenant")
    elif "ouvre Google" in command:
        webbrowser.open_new("https://www.google.ca/?hl=fr")
        talk("google s'ouvre dès maintenant")
    elif "désactive toi" in command:
        talk("j'espère que j'ai fait de mon mieux")
        sys.exit()
    else:
        talk("je n'ai pas compris, pouvez-vous répéter")


if __name__ == '__main__':
    while True:
        the_assistant()
