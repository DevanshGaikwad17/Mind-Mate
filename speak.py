from elevenlabs import ElevenLabs
import pygame
import threading
import os
import time
import tempfile
from contextlib import contextmanager

# Initialize ElevenLabs with your API key
client = ElevenLabs(api_key="your api")

# Create a lock to synchronize access to the ElevenLabs API
engine_lock = threading.Lock()

@contextmanager
def pygame_mixer():
    """Context manager to properly initialize and quit pygame mixer"""
    pygame.mixer.init(frequency=22050)
    try:
        yield
    finally:
        pygame.mixer.quit()

def speak(audio):
    with engine_lock:  # Thread safety for API access
        try:
            # Generate speech
            response = client.text_to_speech.convert(
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                output_format="mp3_44100_128",
                text=audio,
                model_id="eleven_multilingual_v2"
            )
            
            # Use a temporary file instead of a fixed filename
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
                temp_filename = temp_file.name
                # Save the audio content
                for chunk in response:
                    temp_file.write(chunk)
            
            # Play the audio using pygame
            with pygame_mixer():
                try:
                    pygame.mixer.music.load(temp_filename)
                    pygame.mixer.music.play()
                    
                    # Wait for playback to complete
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                        
                finally:
                    pygame.mixer.music.unload()  # Ensure the file is released
                    
        except Exception as e:
            print(f"Error during speech synthesis or playback: {e}")
            
        finally:
            # Clean up the temporary file
            try:
                if 'temp_filename' in locals():
                    os.unlink(temp_filename)
            except Exception as e:
                print(f"Error cleaning up temporary file: {e}")


# Eleven labs api is a paid one so you can use this speak.py code insted of the one given above if you dont want any paid api
'''
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
'''
