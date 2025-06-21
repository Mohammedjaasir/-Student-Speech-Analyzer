from groq import Groq
import os

def get_feedback_from_groq(transcript):
    client = Groq(api_key=os.getenv("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"))

    prompt = f"""
    You are a speaking coach. Analyze this student transcript and give detailed feedback.
    
    Transcript:
    {transcript}
    
    Your feedback should include:
    - Speaking clarity
    - Use of filler words
    - Grammar issues
    - Suggestions to improve
    """

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a speaking coach."},
            {"role": "user", "content": prompt}
        ],
        model="llama3-70b-8192"
    )

    return response.choices[0].message.content
