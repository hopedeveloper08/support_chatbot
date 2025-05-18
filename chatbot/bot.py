import ollama

def model(model_name, prompt):
    response = ollama.chat(
        model=model_name, 
        messages=[{'role': 'user', 'content': prompt}],
        options={"temperature": 0}
    )
    return response['message']['content']
