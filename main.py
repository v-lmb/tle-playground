from fastapi import FastAPI
from app.routers import satellites
from app.database import init_db

# création de l'application FastAPI
app = FastAPI(
    title="TLE Playground",
    description="API pour les données satellitaires TLE",
    version="0.1.0"
)

# création des tables au démarrage
init_db()

# enregistrement du roter satellites
app.include_router(satellites.router)


@app.get("/health")
def health():
    """
    Vérifie que l'API tourne
    """
    return {"status": "ok"}
