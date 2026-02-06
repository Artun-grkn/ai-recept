import cohere

API_key = "BArxOn5os1QnSN1vToWYgfyxr0s7BQblwT0i4Fi8"
co = cohere.Client(API_key)

def chatbot_response(prompt):
    response = co.chat(message=prompt)
    return response.text
