def analyze_text(text, duration_seconds):
    words = text.split()
    wpm = len(words) / (duration_seconds / 60)

    filler_words = ['um', 'uh', 'like', 'you know']
    filler_count = sum(text.lower().count(word) for word in filler_words)

    return {
        "wpm": round(wpm, 2),
        "word_count": len(words),
        "filler_count": filler_count
    }
