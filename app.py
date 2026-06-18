import streamlit as st

from chatbot import generate_response
from prompts import MODES



##NOW WE CREATE THE PAGE TITLE

st.title("🎓 AI STUDY ASSISTANT")


##SIDEBAR

mode = st.sidebar.selectbox(
    "Learning Mode",
    list(MODES.keys())
)


##memory storage

if "messages" not in st.session_state:
    st.session_state.messages = []
    

##user input
user_input = st.chat_input(
    "Ask a question"
)


##response generation

if user_input:
    if len(st.session_state.messages) == 0:
        
        st.session_state.messages.append(
            {
                "role": "system",
                "content": MODES[mode]
            }
        )
    
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    
    
    st.write("Question received")
    
    answer = generate_response(
        st.session_state.messages
    )
    
    st.write(answer)
    
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )



##time to display the chat

for msg in st.session_state.messages:
    
    if msg["role"] == "user":
        st.chat_message("user").write(
            msg["content"]
        )

    elif msg["role"] == "assitant":
        st.chat_message("assistant").write(
            msg["content"]
        )