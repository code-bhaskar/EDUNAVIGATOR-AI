from backend.processor import query_system
import os
from dotenv import load_dotenv

load_dotenv()

try:
    message = "what is pca"
    chat_id = "some_id"
    
    # 1. Test query_system
    results = query_system(message, chat_id=chat_id)
    print("query_system successful")
    
    # 2. Test context creation
    context = "\n".join([r['text'] for r in results]) if results else "No direct academic context found."
    print("context created")
    
    # 3. Test Groq call
    from groq import Groq
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    formatted_history = []
    
    print("Sending message to Groq...")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful academic assistant. Answer based on context if provided."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {message}"}
        ],
        temperature=0.7
    )
    print("Response text:", response.choices[0].message.content)

except Exception as e:
    import traceback
    traceback.print_exc()
