def parse_data(offres):
    """Extrait les données utiles des offres sous forme de 3 listes: offres, entreprises et compétences."""
    offres_list, entreprises_list, competences_list = [], [], []

    for offre in offres:
        offres_list.append({
            "id": offre.get("id"),
            "intitule": offre.get("intitule"),
            "description": offre.get("description"),
            "typeContrat": offre.get("typeContrat"),
            "lieuTravail": offre.get("lieuTravail", {}).get("libelle"),
            "dateCreation": offre.get("dateCreation"),
            "dureeTravailLibelle": offre.get("dureeTravailLibelle"),
            "salaire": offre.get("salaire", {}).get("libelle"),
        })

        entreprise = offre.get("entreprise")
        if entreprise:
            entreprises_list.append({
                "offre_id": offre.get("id"),
                "nom": entreprise.get("nom"),
                "entrepriseAdaptee": entreprise.get("entrepriseAdaptee"),
            })

        for comp in offre.get("competences", []):
            competences_list.append({
                "offre_id": offre.get("id"),
                "competence_code": comp.get("code"),
                "competence_libelle": comp.get("libelle")
            })

    return offres_list, entreprises_list, competences_list
