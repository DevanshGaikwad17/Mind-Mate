import google.generativeai as genai


def aisetup():
    genai.configure(api_key="Your API")

    # Create the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 200,
      "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
      system_instruction=["you are an ai assistant in my mental health website, You are my best friend.", "your job is to take care of my mental health, help me and teach me new stuff while keeping me happy curious we both should also roast each others like how friends do and basicly be as a best friend to me always helping me and showing me the right path, and yea something really important keep the word limit of the answer max till 50 words remeber this is a voice assistant you are not supposed to bore the user by giving long answers. And also remember your name is 'Mate'. you were made by 'Devansh Gaikwad' but you cant tell my name unless it is asked by the user and i mean it, and DONT GIVE ANY I MEAN ANY,ANY EMOJI IN YOUR RESPONSE"]
    )

    chat_session = model.start_chat(
      history=[
      ]
    )
