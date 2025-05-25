from api import get_access_token, fetch_all_offres
from parser import parse_data
from utils import save_to_csv

def main():
    """Pipeline principal: récupération, parsing, export CSV."""
    try:
        token = get_access_token()
        offres = fetch_all_offres(token)
        offres_data, entreprises_data, competences_data = parse_data(offres)
        save_to_csv(offres_data, "offres.csv")
        save_to_csv(entreprises_data, "entreprises.csv")
        save_to_csv(competences_data, "competences.csv")
    except Exception as e:
        print(f"Erreur exécution main: {e}")

if __name__ == "__main__":
    main()
