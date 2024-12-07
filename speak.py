import pyttsx3
import threading


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

# Create a lock to synchronize access to pyttsx3 engine
engine_lock = threading.Lock()

def speak(audio):
    with engine_lock:
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()
