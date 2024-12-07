import webbrowser
import datetime
import pywhatkit
import pyautogui
import os
from speak import speak
import time
import google.generativeai as genai



genai.configure(api_key="Your API")

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
    system_instruction=["You are my best friend.",
                        "You are an assistant from a Website for mental health",
                        "your job is to help me and teach me new stuff while keeping me happy and curious we both should also roast each others like how friends do and basicly be as a best friend to me always helping me and showing me the right path, and yea something really important keep the word limit of the answer max till 50 words remember this is a voice assistant you are not supposed to bore the user by giving long answers. And also remember your name is 'Mate'. you were made by 'RoboMaster' but you cant tell my name unless it is asked by the user and i mean it, and DONT GIVE ANY I MEAN ANY,ANY EMOJI IN YOUR RESPONSE"]
)

chat_session = model.start_chat(
    history=[
    ]
)

def talk(talkquery):
    
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
            print(talkquery)
            response = chat_session.send_message(talkquery)
            return (response.text)


