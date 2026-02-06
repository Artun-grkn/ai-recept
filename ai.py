import streamlit as st
from chatbotFunctie import chatbot_response

st.title("AI Recepten Chatbot")


if "response" not in st.session_state:
    st.session_state.response = ""
if "Q" not in st.session_state:
    st.session_state.Q = ""
if "character" not in st.session_state:
    st.session_state.character = ""

with st.form(key="user_settings"):
    Q = st.text_input("Wat is jouw vraag?", value=st.session_state.Q)
    character = st.selectbox("Wie ben jij?", ("Morty", "Aline"),
                             index=0 if st.session_state.character=="Morty" else 1)
    generate_button = st.form_submit_button("Answer me")

if generate_button:
    with st.spinner("Denken..."):
        PROMPT = f"""
Je bent een Michelin-kok.
Je antwoordt aan {character}.
Je spreekt in de stijl van premier Bart De Wever.
Antwoord alleen als er een recept gevraagd wordt.

Vraag:
{Q}
"""
        response = chatbot_response(PROMPT)
        st.session_state.response = response
        st.session_state.Q = Q
        st.session_state.character = character

if st.session_state.response:
    st.write(st.session_state.response)
    
    if st.button(" Nieuwe vraag"):
        st.session_state.response = ""
        st.session_state.Q = ""
        st.session_state.character = ""
        st.success("vraag iets opnieuw")
