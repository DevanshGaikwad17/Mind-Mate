import speech_recognition as sr
from textblob import TextBlob

def get_emotion_from_text(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # More nuanced emotion detection
    if polarity > 0.5:
        emotion = "very_happy"
    elif polarity > 0:
        emotion = "happy"
    elif polarity < -0.5:
        emotion = "very_sad"
    elif polarity < 0:
        emotion = "sad"
    else:
        if subjectivity > 0.5:
            emotion = "excited"
        else:
            emotion = "neutral"
    
    return emotion

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 500
        try:
            audio = r.listen(source)
            print("Processing...")
            
            query = r.recognize_google(audio, language='en-in')
            print(f"Recognized text: {query}")
            
            emotion = get_emotion_from_text(query)
            print(f"Detected emotion: {emotion}")
            
            return query, emotion

        except Exception as e:
            print(f"An error occurred: {e}")
            return "None", "neutral"

# talking.py
import google.generativeai as genai
# ... (other imports remain the same)

def get_emotion_prompt(emotion):
    emotion_prompts = {
        "very_happy": "I'm in an excellent mood! ",
        "happy": "I'm feeling good! ",
        "neutral": "",
        "sad": "I'm feeling a bit down. ",
        "very_sad": "I'm feeling really sad. ",
        "excited": "I'm really excited! "
    }
    return emotion_prompts.get(emotion, "")
