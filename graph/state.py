from typing import Optional, Dict

class KaduceaState(Dict):
    def __init__(self):
        super().__init__()
        self["route"]: Optional[str] = None  # "devis" ou "renseignement"
        self["collected_data"]: Dict[str, str] = {}  # pour le devis
        self["current_field"]: Optional[str] = None  # champ en cours