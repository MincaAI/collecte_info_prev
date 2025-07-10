import os

def load_prompt_template(name: str) -> str:
    """
    Charge dynamiquement le prompt depuis un fichier texte dans le dossier prompts/.
    Usage : load_prompt_template('devis_agent_prompt') ou load_prompt_template('renseignement_agent_prompt')
    """
    path = os.path.join(os.path.dirname(__file__), '..', 'prompts', f'{name}.txt')
    with open(path, encoding='utf-8') as f:
        return f.read()

def load_prompt(name: str) -> str:
    """
    Alias pour load_prompt_template pour compatibilité avec les imports existants.
    """
    return load_prompt_template(name) 