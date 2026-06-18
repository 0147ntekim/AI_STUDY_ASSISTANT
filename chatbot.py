####the chatbot engine and this gives us conversation memory


from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)



##WE CREATE A RESPONSE FUNCTION

def generate_response(messages):
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            
            messages=messages,
            
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


###notice we pass a messages list

##also we passed in error handling which prevents streamlit from crashing
