import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_assistant(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful chat assistant for students. Answer clearly in simple English."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    question = "What is Artificial Intelligence?"
    answer = chat_assistant(question)

    print("User:", question)
    print("Assistant:", answer)