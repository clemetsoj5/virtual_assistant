import pyttsx3

def output(text):
    my_assistant = pyttsx3.init()
    
    # setting voice of my assitant to a particular type
    tones = my_assistant.getProperty('voices')
    my_assistant.setProperty('voice', tones[0].id)

    my_assistant.say(text)

    my_assistant.runAndWait()


def greet_user():
    # greeting user when the program starts
    output("Hello there, how may I assist you today?")
def input_ready():

    greet_user()


input_ready()