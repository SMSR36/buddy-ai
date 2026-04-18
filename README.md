# Buddy AI 🤖👁️

## 📌 Overview

Buddy AI is an assistive AI system designed to help visually impaired users understand their surroundings using voice commands and real-time image analysis.

The system listens for a wake word ("Hey Buddy"), captures an image using an ESP32-CAM, sends it to Google's Gemini API for analysis, and then speaks out the response while displaying it in the terminal.

---

## 🎯 Key Features

* 🎤 Voice-controlled interaction (wake word detection)
* 📷 Real-time image capture using ESP32-CAM
* 🧠 AI-powered image understanding (Gemini API)
* 🔊 Text-to-speech response for accessibility
* 💻 Terminal output for debugging and monitoring
* 👓 Designed for wearable use (smart glasses for blind assistance)

---

## 🛠️ Tech Stack

* Python
* ESP32-CAM
* Google Gemini API
* SpeechRecognition
* pyttsx3 (Text-to-Speech)
* Requests

---

## ⚙️ System Architecture

1. User says: **"Hey Buddy"**
2. Laptop microphone captures voice input
3. Command is processed using speech recognition
4. ESP32-CAM captures an image
5. Image + command sent to Gemini API
6. AI generates response
7. Output is:

   * 🔊 Spoken via speaker
   * 💻 Printed in terminal

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/buddy-ai.git
cd buddy-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Update Configuration

Replace ESP32 IP:

```python
ESP32_URL = "http://<your-esp32-ip>/capture"
```

Add your Gemini API key:

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

### 4. Run the Project

```bash
python server.py
```

---

## 📸 Future Enhancements

* Wake word detection without Google dependency
* Offline AI support
* Mobile integration
* Battery-powered wearable prototype
* Object detection and navigation assistance

---

## 🌍 Real-World Use Case

This project aims to evolve into a **wearable AI assistant for visually impaired individuals**, where:

* ESP32-CAM is mounted on glasses
* Powered by a portable battery
* Provides real-time scene understanding with voice feedback

---

## ⚠️ Security Note

* Do NOT expose your API keys publicly
* Use environment variables for production

---

## 👤 Author

**Mohan**

---


