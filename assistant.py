
import pyttsx3
import speech_recognition as speech
import webbrowser 
import datetime 
 

def output(text):
    my_assistant = pyttsx3.init()
    
    # setting voice of my assitant to a particular type
    tones = my_assistant.getProperty('voices')
    my_assistant.setProperty('voice', tones[1].id)

    my_assistant.say(text)

    my_assistant.runAndWait()

def whichDay():
     
    currentDay = datetime.datetime.today().weekday()
     

    day_count = {0: 'Monday', 
                1: 'Tuesday',
                2: 'Wednesday', 
                3: 'Thursday',
                4: 'Friday', 
                5: 'Saturday',
                6: 'Sunday'}
     
    if currentDay in day_count.keys():
        week_day = day_count[currentDay]
        print(week_day)
        output("Today is currently " + week_day)

def greet_user():
    # greeting user when the program starts
    output("Hello there, how may I assist you today?")

def input_command():
    in_voice = speech.Recognizer()

    with speech.Microphone() as source:
        print('Listening for command')

        in_voice.pause_threshold = 0.7
        audio = in_voice.listen(source)

        try:
            print("Processing")
            Query = in_voice.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Couldn't quite understand. Could you try again? ")
            return "None"
        return Query

def input_ready():

    greet_user()

    while True:
    
        user_input = input_command().lower()

        if "what day is it" in user_input:
            whichDay()
            continue
        



input_ready()