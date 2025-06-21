# 🧠 Student Speech Analyzer

A Generative AI-powered web app that analyzes student speeches and provides real-time feedback on speaking skills — including clarity, pacing, filler words, and delivery confidence. Built using Streamlit, OpenAI Whisper, and LLaMA 3 via Groq.

---

## 🚀 Features

- 🎙️ Upload or record `.wav` speech files
- 🔤 Converts speech to text using OpenAI Whisper
- 🧠 Analyzes speeches using LLMs via Groq API
- 📊 Generates feedback on:
  - Speaking speed (WPM)
  - Filler word usage
  - Clarity and structure
  - Confidence and tone
- 📥 Download feedback as a clean PDF
- 🌐 Supports multilingual input (future roadmap)

---

## 📁 Project Structure

student-speech-analyzer/
├── app.py # Main Streamlit app
├── record_audio.py # Microphone-based audio recorder
├── transcribe_audio.py # Audio-to-text using Whisper
├── summarize.py # Feedback generator using Groq LLM
├── save_summary.py # PDF export logic
├── requirements.txt # Python dependencies
├── .streamlit/
│ └── secrets.toml # Stores Groq API key
└── assets/
└── sample_audio.wav # Example input file


---

## 🔧 Installation

git clone https://github.com/Mohammedjaasir/-Student-Speech-Analyzerr.git
cd student-speech-analyzer
pip install -r requirements.txt

## 🔑 Set Up Groq API Key

Inside .streamlit/secrets.toml:
GROQ_API_KEY = "your_real_groq_key"

## ▶️ Run the App

streamlit run app.py

## 📌 Example Use Case

A student uploads their presentation audio →
The tool transcribes the speech →
Analyzes their delivery and pacing →
Suggests improvements like "reduce filler words" or "speak slower" →
Exports a feedback PDF for revision or practice

## 🛠 Tech Stack

#Python, Streamlit
#Whisper (OpenAI)
#Groq API (LLaMA 3)
#FPDF (for feedback PDF generation)
#SoundDevice + SciPy (audio capture)

## 📢 Future Enhancements

📈 Visual charts for pacing and filler word frequency
🌐 Multilingual transcription support (Tamil, Hindi, etc.)
🧑‍🏫 Teacher dashboard to track student progress
🎙️ Live analysis mode during presentations

## 🤝 Acknowledgements

Built with ❤️ by Jaax
Original idea inspired by Colin Dorman, who sparked the need for better automated speech feedback tools in education.


