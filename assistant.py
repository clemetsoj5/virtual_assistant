import pyttsx3
import speech_recognition as speech
import datetime 

def output(text):
    my_assistant = pyttsx3.init()
    
    # setting voice of my assitant to a particular type
    tones = my_assistant.getProperty('voices')
    my_assistant.setProperty('voice', tones[1].id)

    my_assistant.say(text)

    my_assistant.runAndWait()

def tellDay():
     
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
     
    #this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        output("The day is " + day_of_the_week)

def greet_user():
    # greeting user when the program starts
    output("Hello there, how may I assist you today?")

def input_command():
    in_voice = speech.Recognizer()

    with speech.Microphone() as source:
        print('Listening for command')

        speech.pause_threshold = 0.7
        audio = speech.listen(source)

        try:
            print("Processing")
            Query = speech.recognize_google(audio, language='en-in')
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
        



input_ready()