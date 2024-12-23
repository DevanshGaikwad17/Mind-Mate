# Import required libraries for different functionalities
import webbrowser  # For opening web pages
import datetime   # For date and time operations
import pywhatkit  # For WhatsApp automation
import pyautogui  # For GUI automation
import os         # For file system operations
from speak import speak  # Custom module for text-to-speech
import time       # For time-related operations
import google.generativeai as genai  # Gemini AI API

# Helper function for consistent debug output formatting
def debug_print(section, message):
    """
    Print debug messages with consistent formatting
    Args:
        section (str): The section/component name
        message (str): The debug message
    """
    print(f"[DEBUG][{section}] {message}")

# Function to map emotions to appropriate conversation starters
def get_emotion_prompt(emotion):
    """
    Convert emotion to conversational context
    Args:
        emotion (str): The detected emotion
    Returns:
        str: Appropriate conversation starter for the emotion
    """
    print(f"\n[DEBUG][Emotion] Processing emotion: {emotion}")
    emotion_prompts = {
        "very_happy": "I'm in an excellent mood! ",
        "happy": "I'm feeling good! ",
        "neutral": "",
        "sad": "I'm feeling a bit down. ",
        "very_sad": "I'm feeling really sad. ",
        "excited": "I'm really excited! "
    }
    result = emotion_prompts.get(emotion, "")
    debug_print("Emotion", f"Generated prompt: {result}")
    return result

# Initialize Gemini AI with API key
try:
    debug_print("Init", "Configuring Gemini API")
    genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your actual API key
    debug_print("Init", "Gemini API configured successfully")
except Exception as e:
    debug_print("ERROR", f"Failed to configure Gemini API: {str(e)}")

# Configure AI model parameters
debug_print("Model", "Initializing model configuration")
generation_config = {
    "temperature": 1,        # Controls response randomness
    "top_p": 0.95,          # Nucleus sampling parameter
    "top_k": 64,            # Top-k sampling parameter
    "max_output_tokens": 100,  # Maximum response length
    "response_mime_type": "text/plain",  # Response format
}

# Initialize the AI model with personality and behavior guidelines
try:
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
            - Keep responses concise and engaging
            '''
        ]
    )
    debug_print("Model", "Model initialized successfully")
except Exception as e:
    debug_print("ERROR", f"Failed to initialize model: {str(e)}")

# Initialize chat session for ongoing conversation
try:
    debug_print("Chat", "Starting chat session")
    chat_session = model.start_chat(history=[])
    debug_print("Chat", "Chat session started successfully")
except Exception as e:
    debug_print("ERROR", f"Failed to start chat session: {str(e)}")

# Main function to process and respond to user queries
def talk(talkquery, emotion="neutral"):
    """
    Process user queries and generate appropriate responses
    Args:
        talkquery (str): The user's query
        emotion (str): The detected emotion (default: "neutral")
    Returns:
        str: Response text for general queries
    """
    debug_print("Talk", f"Received query: '{talkquery}' with emotion: {emotion}")
    
    # Handle WhatsApp messaging
    if 'send whatsapp message' in talkquery:
        debug_print("WhatsApp", "Processing WhatsApp message command")
        swin = talkquery.replace("send whatsapp message", "")
        swin = swin.replace("to", "")
        sen = swin[-11:]  # Extract phone number
        swin = swin.replace(swin[-11:], "")  # Extract message
        debug_print("WhatsApp", f"Sending message: '{swin}' to: {sen}")
        try:
            pywhatkit.sendwhatmsg_instantly("+91" + sen, swin)
            debug_print("WhatsApp", "Message sent successfully")
        except Exception as e:
            debug_print("ERROR", f"Failed to send WhatsApp message: {str(e)}")

    # Handle chess game request
    elif 'play' in talkquery and 'chess' in talkquery:
        debug_print("Chess", "Opening chess game")
        speak("yes, sure")
        webbrowser.open("https://www.chess.com/play/computer")

    elif 'who created you' in talkquery:
        debug_print("Query", "Responding to creator inquiry")
        speak("I was created by RoboMaster")

    # Time query
    elif 'time' in talkquery:
        debug_print("Time", "Processing time query")
        hour = int(datetime.datetime.now().hour)
        min = int(datetime.datetime.now().minute)
        ab = "am" if hour < 12 else "pm"
        strTime = time.strftime("%I:%M" + ab)
        debug_print("Time", f"Current time: {strTime}")
        speak(f"the time is {strTime}")

    # Date query
    elif 'date' in talkquery:
        debug_print("Date", "Processing date query")
        current_date = time.strftime("%d-%m-%Y")
        debug_print("Date", f"Current date: {current_date}")
        speak(current_date)

    # Weather query
    elif 'weather' in talkquery:
        debug_print("Weather", "Opening weather website")
        webbrowser.open("https://www.google.com/search?q=weather")

    # News query
    elif 'news' in talkquery:
        debug_print("News", "Opening news website")
        webbrowser.open("https://www.youtube.com/watch?v=nyd-xznCpJc")

    # SOS message
    elif 'sos' in talkquery:
        debug_print("SOS", "Sending emergency messages")
        h = 9886093707
        try:
            for i in range(3):
                debug_print("SOS", f"Sending message {i+1}/3")
                pywhatkit.sendwhatmsg_instantly("+91" + str(h), "Its an emergency help!")
        except Exception as e:
            debug_print("ERROR", f"Failed to send SOS message: {str(e)}")

    # Photos query
    elif 'show' in talkquery and 'family photos' in talkquery:
        debug_print("Photos", "Opening Google Photos")
        speak("ok")
        webbrowser.open("https://photos.google.com/")

    # Music playback
    elif 'play' in talkquery and 'music' in talkquery:
        debug_print("Music", "Attempting to play music")
        speak("ok")
        try:
            music_dir = 'C:\\Users\\devan\\Music\\Playlists'
            songs = os.listdir(music_dir)
            debug_print("Music", f"Found {len(songs)} songs in playlist")
            os.startfile(os.path.join(music_dir, songs[1]))
            debug_print("Music", "Started playing music")
        except Exception as e:
            debug_print("ERROR", f"Failed to play music: {str(e)}")

    # Open application
    elif "open" in talkquery:
        app_name = talkquery.replace("open", "").strip()
        debug_print("App", f"Attempting to open application: '{app_name}'")
        try:
            pyautogui.press("super")
            time.sleep(1)
            pyautogui.typewrite(app_name)
            time.sleep(1)
            pyautogui.press("enter")
            debug_print("App", "Application command executed")
        except Exception as e:
            debug_print("ERROR", f"Failed to open application: {str(e)}")
else:
if talkquery != "none":
    debug_print("Chat", "Processing general query")
    # Add emotional context to the query
    emotion_context = get_emotion_prompt(emotion)
    augmented_query = emotion_context + talkquery
    debug_print("Chat", f"Augmented query: '{augmented_query}'")
    
    try:
        response = chat_session.send_message(augmented_query)
        debug_print("Chat", f"Got response: '{response.text}'")
        return response.text
    except Exception as e:
        debug_print("ERROR", f"Failed to get chat response: {str(e)}")
        return "I encountered an error processing your request."

