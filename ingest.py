import requests
from dotenv import load_dotenv
from sqlalchemy import select
from datetime import datetime, timezone

from app.database import init_db, SessionLocal
from app.models import Satellite

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


def save_satellites(satellites):
    """
    Sauvegarde une liste de satellites en base (upsert)
    Args:
        satellites
    """
    # ouvre une session - espace de travail
    session = SessionLocal()

    try:
        inserted = 0
        updated = 0

        for sat in satellites:
            # chercher si le satellite existe déjà en base
            existing = session.execute(
                select(Satellite).where(Satellite.name == sat["name"])
            ).scalar_one_or_none()

            if existing is None:
                # n'existe pas -> créer le nouvel objet et l'ajoute
                new_sat = Satellite(
                    name=sat["name"],
                    line1=sat["line1"],
                    line2=sat["line2"]
                )
                session.add(new_sat)
                inserted += 1
            else:
                # si existe déjà -> mise à jour de ses données
                existing.line1 = sat["line1"]
                existing.line2 = sat["line2"]
                existing.updated_at = datetime.now(timezone.utc)
                updated += 1

        # écrit tout en base d'un coup
        session.commit()
        print(f"Ingestion terminée : {inserted} insérés, {updated} mis à jour.")

    except Exception as e:
        # en cas d'erreur, tout est annulé, rien n'est écrit
        session.rollback()
        print(f"Erreur : {e}")

    finally:
        # on ferme toujours la session
        session.close()


if __name__ == "__main__":
    init_db()
    satellites = fetch_tle()
    save_satellites(satellites)
