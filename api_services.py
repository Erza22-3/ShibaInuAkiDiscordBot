
import os
import requests

async def generate_discussion_questions(num_people, duration_mins, mood, topic_preferences, question_types):
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return "Error: Valid DEEPSEEK_API_KEY not found in environment variables."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""Generate 3 sets of {num_people} profound questions that reveal deep insights about life and human experience.
Duration: {duration_mins} minutes
Current mood: {mood}
Preferred topics: {', '.join(topic_preferences)}
Question types: {', '.join(question_types)}

Format the response as:
Set 1:
- 
- 

Set 2:
- 
- 

Focus on questions that challenge assumptions and provoke genuine self-reflection."""

    data = {
        "model": "deepseek-reasoner",
        "messages": [
            {
                "role": "system",
                "content": "You are a skilled discussion facilitator that creates engaging questions for group conversations."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1000
    }

    try:
        response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating questions: {str(e)}"
