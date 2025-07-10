# Kaducea – Agent conversationnel (Devis & Renseignement)

## Description
Kaducea est un agent conversationnel capable de répondre à des questions (RAG via Pinecone) ou de collecter des informations pour un devis, avec consentement RGPD, orchestré par LangGraph et affiché dans une interface Streamlit.

## Lancer le projet

1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Lancez l'interface Streamlit :
   ```bash
   streamlit run main.py
   ```

## Structure du projet
- `main.py` : point d'entrée Streamlit
- `graph/` : définition du flow LangGraph et des noeuds
- `rag/` : intégration Pinecone

## Configuration
- Ajoutez vos clés API Pinecone et OpenAI dans un fichier `.env` à la racine du projet.

## À faire
- Compléter les prompts RAG
- Finaliser la collecte d'informations pour le devis
- Ajouter la gestion du contexte utilisateur 