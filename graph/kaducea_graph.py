from typing import Dict, Optional, Tuple, TypedDict, Any
from agents.orchestrator import orchestrator_agent
from agents.langchain_devis_agent import run_devis_chain
from agents.langchain_renseignement_agent import run_renseignement_chain

class KaduceaState(TypedDict):
    route: Optional[str]
    collected_data: Dict[str, Any]
    current_field: Optional[str]

class KaduceaGraph:
    def __init__(self):
        # State minimal : route + données collecte (si devis)
        self.state: KaduceaState = {
            "route": None,
            "collected_data": {},
            "current_field": None
        }
        self.history = [
            ("assistant", "👋 Bonjour et bienvenue chez Kaducea !\nJe suis votre assistant virtuel pour vous accompagner dans votre premier entretien de prévoyance.\nJe vais simplement vous poser quelques questions pour mieux comprendre votre situation, et vous guider pas à pas.\nAvant de commencer, auriez-vous des questions?")
        ]  # [(role, content)]

    def process(self, user_input: str) -> Tuple[str, KaduceaState]:
        # from agents.orchestrator import is_devis_request
        # 1. Toujours vérifier si c'est une demande de devis, peu importe le flow courant
        # last_assistant_message = None
        # for role, content in reversed(self.history):
        #     if role == "assistant":
        #         last_assistant_message = content
        #         break
        # if is_devis_request(user_input, last_assistant_message=last_assistant_message):
        #     self.state["route"] = "devis"
        #     # On reset les données de collecte et le champ courant
        #     self.state["collected_data"] = {}
        #     self.state["current_field"] = None
        #     self.history.append(("user", user_input))
        #     response = run_devis_chain(self.history, user_input)
        #     self.history.append(("assistant", response))
        #     return str(getattr(response, 'content', response)), self.state

        # route = self.state.get("route")

        # # Toujours reclassifier si route est None, accueil ou inconnu
        # if route is None or route in ("accueil", "inconnu"):
        #     print(f"[DEBUG] Appel de l'agent ORCHESTRATOR avec user_input: {user_input}")
        #     orchestrator_result = orchestrator_agent({"user_input": user_input})
        #     route = orchestrator_result.get("route")
        #     self.state["route"] = route

        #     if route == "devis":
        #         self.state["collected_data"] = {}
        #         self.state["current_field"] = None
        #         # NE PAS vider l'historique ici
        #         self.history.append(("user", user_input))
        #         response = run_devis_chain(self.history, user_input)
        #         self.history.append(("assistant", response))
        #         return str(getattr(response, 'content', response)), self.state
        #     elif route == "renseignement":
        #         # NE PAS vider l'historique ici
        #         self.history.append(("user", user_input))
        #         response = run_renseignement_chain(self.history, user_input)
        #         self.history.append(("assistant", response))
        #         return str(getattr(response, 'content', response)), self.state
        #     elif route == "accueil":
        #         response = "Bonjour ! Je suis KaducéaAI, votre assistant virtuel en contrat prevoyance. Souhaitez-vous réaliser un devis, ou aimeriez-vous des informations ?"
        #         return response, self.state
        #     else:
        #         return "Désolé, je n'ai pas compris votre demande.", self.state

        # # 2. Flow DEVIS
        # if route == "devis":
        #     print(f"[DEBUG] Appel de l'agent DEVIS avec user_input: {user_input}")
        #     self.history.append(("user", user_input))
        #     response = run_devis_chain(self.history, user_input)
        #     self.history.append(("assistant", response))
        #     return str(getattr(response, 'content', response)), self.state

        # # 3. Flow RENSEIGNEMENT
        # if route == "renseignement":
        #     print(f"[DEBUG] Appel de l'agent RENSEIGNEMENT avec user_input: {user_input}")
        #     self.history.append(("user", user_input))
        #     response = run_renseignement_chain(self.history, user_input)
        #     self.history.append(("assistant", response))
        #     return str(getattr(response, 'content', response)), self.state

        # # 4. Catch-all fallback
        # print(f"[DEBUG] Fallback: route inconnue, user_input: {user_input}")
        # return "Désolé, une erreur s'est produite.", self.state

        # Nouvelle logique : tout passe par l'agent devis
        self.history.append(("user", user_input))
        response = run_devis_chain(self.history, user_input)
        self.history.append(("assistant", response))
        return str(getattr(response, 'content', response)), self.state

def get_kaducea_graph() -> KaduceaGraph:
    return KaduceaGraph()
