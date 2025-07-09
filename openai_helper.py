import openai

client = openai.OpenAI(api_key="sk-...")  # Should Replace with our OpenAI API key

def generate_code(prompt):
    system_prompt = "You're a Python coding assistant. Write clean, correct code only. Then explain it in 2-3 sentences."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
