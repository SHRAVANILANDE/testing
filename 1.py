import pyttsx3
import os
import webbrowser

a=input("Enter your name:")
pyttsx3.speak("welcome")
pyttsx3.speak(a)
pyttsx3.speak("how can i  help you")
b=input("how can i help you?\n")
if("run" in b) or ("open chrome"in b) or("start chrome"in b):
    pyttsx3.speak("opening chrome")
    print(os.system("start chrome"))
elif("paint" in b) or ("draw" in b):
        pyttsx3.speak("opening paint")
        print(os.system("Mspaint"))
elif("calci"in b) or ("calculator" in b):
        pyttsx3.speak("opening calculator")
        print(os.system("calc"))
elif("amway india"in b) or("amway"in b)or ("amway website"in b ):
    pyttsx3.speak("opening amway")
    print(webbrowser.open('http://amwayindia.com', new=2))
elif("how many cpu's"in b):
    print(os.cpu_count())
elif("who is the user"in b):
    print(os.getlogin())

    