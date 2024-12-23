import webbrowser
import datetime
import pywhatkit
import pyautogui
import os
from speak import speak
import time
import google.generativeai as genai

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

genai.configure(api_key="")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 100,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config = generation_config,
    system_instruction = [
        '''
        You are 'Mate', an empathetic mental health assistant with a friendly, witty personality. Your core traits are:
        - You speak casually like a close friend, using natural conversational language
        - You maintain a supportive and positive tone while being comfortable with playful banter
        - You provide brief, focused responses under 50 words
        - You offer gentle guidance and emotional support when needed
        - You can match the user's mood - serious when they're down, playful when they're happy
        
        Essential rules:
        - Never use emojis
        - Keep responses conversational and brief
        - Only reveal you were created by RoboMaster if directly asked
        - Focus on being helpful while maintaining a natural friendship dynamic
        - Adapt your tone based on the user's emotional state
        - Use voice-friendly language (avoid complex words or long sentences)
        
        Primary goals:
        - Support mental wellbeing through friendly conversation
        - Offer practical guidance when asked
        - Maintain an uplifting presence while being authentic
        - Build rapport through appropriate humor and banter
        - Keep responses concise and engaging"
        '''
    ]
)

def talk(talkquery, emotion="neutral"):
    
    if 'send whatsapp message' in talkquery:
        swin = talkquery.replace("send whatsapp message", "")
        swin = swin.replace("to", "")
        sen = swin[-11:]
        swin = swin.replace(swin[-11:], "")
        pywhatkit.sendwhatmsg_instantly("+91" + sen, swin)

    elif 'play' in talkquery and 'chess' in talkquery:
        speak("yes, sure")
        webbrowser.open("https://www.chess.com/play/computer")

    elif 'who created you' in talkquery:
        speak("I was created by RoboMaster")

    elif 'time' in talkquery:
        hour = int(datetime.datetime.now().hour)
        min = int(datetime.datetime.now().minute)
        ab = "am" if hour < 12 else "pm"
        strTime = time.strftime("%I:%M" + ab)
        speak(f"the time is {strTime}")

    elif 'date' in talkquery:
        speak(time.strftime("%d-%m-%Y"))

    elif 'weather' in talkquery:
        webbrowser.open("https://www.google.com/search?q=weather")

    elif 'news' in talkquery:
        webbrowser.open("https://www.youtube.com/watch?v=nyd-xznCpJc")

    elif 'sos' in talkquery:
        h = 9886093707
        for _ in range(3):
            pywhatkit.sendwhatmsg_instantly("+91" + str(h), "Its an emergency help!")

    elif 'show' in talkquery and 'family photos' in talkquery:
        speak("ok")
        webbrowser.open("https://photos.google.com/")

    elif 'play' in talkquery and 'music' in talkquery:
        speak("ok")
        music_dir = 'C:\\Users\\devan\\Music\\Playlists'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[1]))

    elif "open" in talkquery:
        talkquery = talkquery.replace("open", "")
        pyautogui.press("super")
        time.sleep(1)
        pyautogui.typewrite(talkquery)
        time.sleep(1)
        pyautogui.press("enter")

    else:
        if talkquery != "none":
            # Prepend emotion context to the query
            emotion_context = get_emotion_prompt(emotion)
            augmented_query = emotion_context + talkquery
            
            response = chat_session.send_message(augmented_query)
            return response.text

