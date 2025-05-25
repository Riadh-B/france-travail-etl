import requests
import os
from dotenv import load_dotenv
import json
import logging

load_dotenv()

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("francetravail_api")



def get_access_token():
    """Récupère le token d'accès OAuth2 nécessaire aux requêtes API."""
    try:
        data = {
            'grant_type': 'client_credentials',
            'client_id': os.getenv("CLIENT_ID"),
            'client_secret': os.getenv("CLIENT_SECRET"),
            'scope': os.getenv("API_SCOPE"),
        }
        response = requests.post(os.getenv("TOKEN_URL"), data=data)
        response.raise_for_status()
        return response.json().get("access_token")
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du token: {e}")
        raise


def fetch_all_offres(token, departement="07", contrat="CDI"):
    """Récupère toutes les offres d'emploi filtrées par département et type de contrat."""
    url = os.getenv("URL_API")
    headers = {"Authorization": f"Bearer {token}"}
    params = {"departement": departement, "typeContrat": contrat, "range": "0-149"}

    offres = []
    batch_size = 150

    try:
        # Premier appel pour déterminer le nombre total d'offres
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        total = data.get("filtresPossibles", [{}])[0].get("agregation", [{}])[0].get("nbResultats", 0)
        offres.extend(data.get("resultats", []))
        logger.info(f"{len(offres)} offres récupérées sur {total}")

        for start in range(batch_size, total, batch_size):
            end = start + batch_size - 1
            params["range"] = f"{start}-{end}"
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            offres.extend(data.get("resultats", []))
            logger.info(f"Offres [{start}-{end}] récupérées")

        return offres
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des offres: {e}")
        raise