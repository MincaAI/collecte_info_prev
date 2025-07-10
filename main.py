import streamlit as st
from graph.kaducea_graph import get_kaducea_graph
import traceback

from dotenv import load_dotenv
load_dotenv()

# Configuration simple
st.set_page_config(page_title="Chat Kaducea", page_icon="💬")
st.subheader("💬 Votre assistant prévoyance Kaducea")

# Initialisation
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'graph' not in st.session_state:
    st.session_state.graph = get_kaducea_graph()

if not st.session_state.messages:
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "👋 Bonjour et bienvenue chez Kaducea !\n"
            "Je suis votre assistant virtuel pour vous accompagner dans votre premier entretien de prévoyance.\n"
            "Je vais simplement vous poser quelques questions pour mieux comprendre votre situation, et vous guider pas à pas.\n"
            "Avant de commencer, auriez-vous des questions ?"
        )
    })

# Affichage des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input utilisateur
if prompt := st.chat_input("Votre message..."):
    # Afficher le message utilisateur
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Générer et afficher la réponse
    with st.chat_message("assistant"):
        try:
            response, state = st.session_state.graph.process(prompt)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Debug: afficher l'état actuel (optionnel)
            if st.checkbox("Afficher l'état de debug"):
                st.json(state)
                
        except Exception as e:
            error_msg = f"Erreur: {str(e)}"
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            # Debug: afficher la trace complète
            if st.checkbox("Afficher les détails de l'erreur"):
                st.code(traceback.format_exc())

# Bouton pour réinitialiser la conversation
if st.sidebar.button("Nouvelle conversation"):
    st.session_state.messages = []
    st.session_state.graph = get_kaducea_graph()
    st.rerun() 