import streamlit as st
import tempfile
from dotenv import load_dotenv
import os

from audio_utils.transcriber import transcribe_audio
from analysis.analyzer import analyze_text
from feedback.groq_feedback import get_feedback_from_groq

# Load .env
load_dotenv()

st.title("🎙️ Student Speaking Analyzer")

audio_file = st.file_uploader("Upload a student's audio", type=["mp3", "wav"])

if audio_file:
    st.audio(audio_file, format="audio/mp3")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    st.info("🔄 Transcribing audio...")
    transcript, duration = transcribe_audio(tmp_path)

    st.subheader("📝 Transcript")
    st.write(transcript)

    st.info("📊 Analyzing speech...")
    analysis = analyze_text(transcript, duration)

    st.subheader("📈 Analysis Results")
    st.write(f"🕒 Words Per Minute: **{analysis['wpm']}**")
    st.write(f"📄 Total Words: **{analysis['word_count']}**")
    st.write(f"😬 Filler Words: **{analysis['filler_count']}**")

    st.info("💡 Generating AI feedback...")
    feedback = get_feedback_from_groq(transcript)

    st.subheader("🧠 AI Feedback (Groq)")
    st.write(feedback)
