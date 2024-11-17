from talking import talk
from take_command import takeCommand
from speak import speak

def pls():
    query = takeCommand().lower()
    if 'sleep' in query:
        talkquery = query
        talk(talkquery)
        query = "none"
    else:
        talkquery = query
        talk(talkquery)
        query = "none"
    #similarity search
    #hugging face
    #kaggle
