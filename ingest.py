import requests
from dotenv import load_dotenv
import os

# Pour charger les variables du fichier . env
load_dotenv()

# URL CELESTRAK - groupe de stations (ISS, CSS, etc....)
CELESTARK_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"


def fetch_tle():
    """
    Récupère les TLE depuis Celestrak et retourne une liste de disct
    """

    # 1- envoie de la requete HTTP GET
    response = requests.get(CELESTARK_URL, timeout=10)

    # 2- Vérifie que c'est bien passé (lève une erreur si code != 200)
    response.raise_for_status()

    # 3- Découpe de txt brute en liste de lignes
    # strip() enlève les espaces et retours à la ligne en début et fin
    lines = response.text.strip().splitlines()
    satellites = []

    # 4- Parcours des lignes 3 par 3
    for i in range(0, len(lines), 3):
        # NOM
        name = lines[i].strip()
        # LIGNE 1 : DONNEES ORBITALES
        line1 = lines[i + 1].strip()
        # LIGNE 2 : DONNEES ORBITALES
        line2 = lines[i + 2].strip()

        satellites.append({
            "name": name,
            "line1": line1,
            "line2": line2
        })
        return satellites


if __name__ == "__main__":
    satellites = fetch_tle()

    # Affiche les 3 premiers pour vérifier
    for sat in satellites[:3]:
        print(sat)
