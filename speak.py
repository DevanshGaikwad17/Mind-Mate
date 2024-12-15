from elevenlabs import ElevenLabs
import pygame  # For playing audio
import threading
import os
import time

# Initialize ElevenLabs with your API key
client = ElevenLabs(api_key="your api")

# Create a lock to synchronize access to the ElevenLabs API
engine_lock = threading.Lock()

def speak(audio):
    # Lock to ensure thread safety when accessing the ElevenLabs API
    with engine_lock:
        # Generate speech (this returns a generator, so we need to handle it)
        response = client.text_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",  # Example voice ID (replace with actual)
            output_format="mp3_44100_128",  # MP3 format
            text=audio,
            model_id="eleven_multilingual_v2"  # Model ID
        )

        # Generate a unique file name using a timestamp
        filename = "output.mp3"

        # Check if the file already exists and delete it to avoid permission issues
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception as e:
                print(f"Error deleting existing file: {e}")

        # Save the audio content to a unique file
        try:
            with open(filename, "wb") as f:
                for chunk in response:
                    f.write(chunk)
            print(f"Audio saved as {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")
            return

        # Initialize pygame mixer for audio playback
        pygame.mixer.init(frequency=22050)  # Ensure pygame is initialized with a valid frequency

        # Wait for the mixer to be ready
        try:
            pygame.mixer.music.load(filename)
        except Exception as e:
            print(f"Error loading audio file: {e}")
            return

        # Play the audio
        pygame.mixer.music.play()

        # Wait until the audio finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

# Example of calling the speak function
speak("Hello, how are you today?")
