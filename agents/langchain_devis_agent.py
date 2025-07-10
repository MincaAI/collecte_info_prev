from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from graph.prompts import load_prompt
import os
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1,
    api_key=SecretStr(api_key)
)

prompt_template = PromptTemplate(
    input_variables=["system_prompt", "history", "input"],
    template=(
        "{system_prompt}\n"
        "Historique de la conversation :\n{history}\n"
        "Utilisateur : {input}\n"
        "Assistant :"
    )
)

def run_devis_chain(history, user_input):
    """
    Appelle le LLM avec le prompt système, l'historique formaté et l'input utilisateur.
    history : liste de tuples (role, content)
    user_input : str
    """
    system_prompt = load_prompt('DEVIS_AGENT_PROMPT')
    # Formate l'historique pour le prompt
    history_str = "\n".join([
        f"{role.capitalize()} : {content}" for role, content in history
    ])
    chain = prompt_template | llm
    return chain.invoke({"system_prompt": system_prompt, "history": history_str, "input": user_input})

# Instance par défaut pour la compatibilité
devis_agent = run_devis_chain([], "") 