import pandas as pd
import logging

def save_to_csv(data, filename):
    """Sauvegarde les données sous forme de fichier CSV."""
    try:
        pd.DataFrame(data).to_csv(filename, index=False)
        logging.info(f"Fichier sauvé: {filename}")
    except Exception as e:
        logging.error(f"Erreur lors de la sauvegarde du fichier {filename}: {e}")
        raise