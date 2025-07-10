from langchain_openai import ChatOpenAI
from typing import Dict
import os
from dotenv import load_dotenv
from pydantic import SecretStr
from typing import Optional
load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

llm = ChatOpenAI(model="gpt-4o", temperature=0.1, api_key=SecretStr(api_key))

CLASSIFIER_PROMPT = (
    "Tu es un assistant qui doit classifier l'intention d'un utilisateur dans le domaine de la prévoyance pour professionnels de santé.\n"
    "Si l'utilisateur veut un devis, réponds strictement par le mot : devis.\n"
    "Si l'utilisateur veut juste une information, réponds strictement par le mot : renseignement.\n"
    "Si l'utilisateur dit juste bonjour, salut, ou une formule de politesse, réponds strictement par le mot : accueil.\n"
    "Sinon, réponds strictement par le mot : inconnu.\n"
    "Message utilisateur : {input}"
)

def classify_intent(user_input: str) -> str:
    prompt = CLASSIFIER_PROMPT.format(input=user_input)
    print("DEBUG prompt envoyé au LLM:", prompt)
    response = llm.invoke(prompt)
    print("DEBUG LLM response:", response)
    print("DEBUG LLM response type:", type(response))
    # On tente d'accéder à .content, sinon on affiche tout
    try:
        content = response.content
    except AttributeError:
        content = response
    print("DEBUG LLM content:", content)
    intent = str(content).strip().lower()
    if "devis" in intent:
        return "devis"
    if "renseignement" in intent:
        return "renseignement"
    if "accueil" in intent:
        return "accueil"
    if "inconnu" in intent:
        return "inconnu"
    return "inconnu"

def is_devis_request(user_input: str, last_assistant_message: Optional[str] = None) -> bool:
    ACCUEIL_KEYWORDS = [
        "bienvenue chez kaducea",
        "premier entretien de prévoyance",
        "on commence ?"
    ]
    # Prétraitement : détection large d'accord dans la phrase
    ACCEPTANCE_KEYWORDS = [
        "ok", "oui", "c'est parti", "on commence", "go", "d'accord", "let's go", "c'est bon",
        "je suis prêt", "je suis prete", "allons y", "allons-y", "vas-y", "go go", "partons", "top", "c'est ok"
    ]
    user_input_lower = user_input.lower()
    if last_assistant_message and any(k in last_assistant_message.lower() for k in ACCUEIL_KEYWORDS):
        if any(acc in user_input_lower for acc in ACCEPTANCE_KEYWORDS):
            return True
        # Utilise le LLM pour détecter une acceptation large, même si la phrase contient autre chose
        prompt = (
            "Réponds strictement par 'oui' si le message utilisateur contient une formule d'accord, d'acceptation ou d'enthousiasme "
            "pour commencer un entretien de prévoyance, même si la phrase contient une salutation ou autre chose. "
            "Sinon réponds strictement par 'non'.\n"
            f"Message utilisateur : {user_input}"
        )
        response = llm.invoke(prompt)
        content = str(getattr(response, 'content', response)).strip().lower()
        if content == "oui":
            return True
    prompt = (
        "Réponds strictement par 'oui' si le message utilisateur est une demande explicite de devis prévoyance, "
        "sinon réponds strictement par 'non'.\n"
        f"Message utilisateur : {user_input}"
    )
    response = llm.invoke(prompt)
    content = str(getattr(response, 'content', response)).strip().lower()
    return content == "oui"

def orchestrator_agent(state: Dict) -> Dict:
    user_input = state.get("user_input", "").strip()
    intent = classify_intent(user_input)
    return {"route": intent}