import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception:
        return "None"
    return query