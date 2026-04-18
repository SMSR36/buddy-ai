import requests
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# ESP32 camera URL
ESP32_URL = "http://10.105.66.162/capture"

# Gemini API setup
genai.configure(api_key="AIzaSyAE2nM_NMnjkfQckpNziW7JGJLEAFGyYwY")
for m in genai.list_models():
    print(m.name)
model = genai.GenerativeModel("gemini-2.5-flash")
# voice engine
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

def capture_image():
    print("Capturing image...")
    r = requests.get(ESP32_URL)
    return r.content

def analyze(image_bytes, prompt):

    response = model.generate_content(
        [
            prompt,
            {
                "mime_type": "image/jpeg",
                "data": image_bytes
            }
        ]
    )

    return response.text


recognizer = sr.Recognizer()

print("Buddy AI system ready")

while True:

    with sr.Microphone() as source:

        print("Listening...")
        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        if "buddy" in command.lower():

            speak("Analyzing")

            img = capture_image()

            answer = analyze(img, command)

            speak(answer)

    except Exception as e:
        print("Could not understand:", e)