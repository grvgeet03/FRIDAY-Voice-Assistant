import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "2dc484a70c8e47538cae430344cc3a7a"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Only use the below code is you have paid subscription of OpenAI. Use that API key and apply it in this code to enhance the functionality of this code

# def aiProcess(command):
#     client = OpenAI(api_key="<Your Key Here>",  #Insert your OpenAI API key here
#     )

#     completion = client.chat.completions.create(
#     model="gpt-4.0-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
#     )
 
def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif  c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
                
    # If you have the API key, uncomment this code

    # else:
    #     # Let OpenAI handle the request
    #     output = aiProcess(c)
    #     speak(output) 


if __name__ == "__main__":
    speak("Initializing Friday.....")

    while True:
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)

            word = r.recognize_google(audio)

            if (word.lower() == "friday") or (word.lower() == "hey friday"):
                speak("Yes Master!")
                
                with sr.Microphone() as source:
                    print("Friday Active...")
                    audio = r.listen(source,timeout=3, phrase_time_limit=3)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error{e}")