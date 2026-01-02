def analyze_prompt(text):
    text = text.lower()

    emotions = {
        "sad": ["sad", "lonely", "hurt", "cry", "depressed"],
        "angry": ["angry", "mad", "frustrated", "annoyed"],
        "happy": ["happy", "excited", "love", "great"],
        "confused": ["confused", "unsure", "lost", "overthinking"]
    }

    intents = {
        "breakup": ["breakup", "leave", "end relationship"],
        "dating": ["date", "crush", "like someone"],
        "trust": ["trust", "cheating", "lying"],
        "communication": ["talk", "communicate", "argument"]
    }

    detected_emotion = "neutral"
    detected_intent = "general advice"

    for emotion, keywords in emotions.items():
        if any(word in text for word in keywords):
            detected_emotion = emotion
            break

    for intent, keywords in intents.items():
        if any(word in text for word in keywords):
            detected_intent = intent
            break

    return {
        "emotion": detected_emotion,
        "intent": detected_intent,
        "summary": f"The user seems {detected_emotion} and is seeking help related to {detected_intent}."
    }


# Example usage
if __name__ == "__main__":
    user_input = input("Enter your relationship concern: ")
    result = analyze_prompt(user_input)
    print(result)
