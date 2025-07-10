FIELDS_LABELS = {
    # 1. Contexte professionnel
    "lieu_exercice": "Quel est votre lieu d'exercice ?",
    "remplacant": "Êtes-vous remplaçant ? (oui/non ou précisions)",
    "type_collaboration": "Quel est votre type de collaboration (collaborateur, associé, etc.) ?",
    "mode_exercice": "Exercez-vous seul ou en groupe ?",
    "pratique_particuliere": "Avez-vous une pratique particulière (chirurgie, acupuncture, etc.) ?",
    # 2. État civil
    "nom_prenom": "Quel est votre nom et prénom ?",
    "date_naissance": "Quelle est votre date de naissance ?",
    "lieu_naissance": "Quel est votre lieu de naissance ?",
    "telephone": "Quel est votre numéro de téléphone ?",
    "email": "Quelle est votre adresse email ?",
    "adresse_postale": "Quelle est votre adresse postale ?",
    "statut_marital": "Quel est votre statut marital ?",
    "nombre_enfants_a_charge": "Combien d'enfants avez-vous à charge ?",
    "fumeur": "Êtes-vous fumeur ? (oui/non)",
    "sports_a_risques": "Pratiquez-vous des sports à risques ? (liste ou texte libre)",
    # 3. Informations sur l'entreprise
    "denomination_sociale": "Quelle est la dénomination sociale de votre entreprise ?",
    "micro_bnc": "Êtes-vous en micro-BNC ? (oui/non)",
    "date_creation": "Quelle est la date de création de l'entreprise ?",
    "siret": "Quel est le numéro SIRET ?",
    "contrats_en_cours": "Avez-vous des contrats en cours ? (précisez)",
    # 4. Contrats déjà existants
    "prevoyance_existante": "Avez-vous une prévoyance existante ?",
    "sante_existante": "Avez-vous une complémentaire santé existante ?",
    "retraite_existante": "Avez-vous une retraite existante ?",
    "epargne_existante": "Avez-vous une épargne existante ?",
    "commentaires_contrats_existants": "Commentaires sur vos contrats existants (exclusions, expériences passées, refus de prise en charge, etc.) ?",
    # 5. Revenus et frais
    "revenu_n_1": "Quel est votre revenu N-1 ?",
    "revenu_n_2": "Quel est votre revenu N-2 ?",
    "revenu_n_3": "Quel est votre revenu N-3 ?",
    "frais_generaux_n_1": "Quels sont vos frais généraux N-1 ?",
    "commentaires_revenus": "Commentaires sur vos revenus (ex : changement de statut à venir, arrivée d'un associé, achat de locaux…) ?"
}

def get_field_label(field):
    return FIELDS_LABELS.get(field, f"Merci de renseigner : {field}")

def is_question(text):
    if not text:
        return False
    text = text.strip().lower()
    return (
        text.endswith('?') or
        text.startswith('qu\'est-ce') or
        text.startswith('c\'est quoi') or
        text.startswith('pourquoi') or
        text.startswith('comment') or
        text.startswith('quelle') or
        text.startswith('quand') or
        text.startswith('où')
    ) 