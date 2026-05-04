from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import SessionLocal
from app.models import Satellite
from app.schemas import SatelliteSchema

# Router (équivalent d'un Blueprint Flask)
router = APIRouter(
    prefix="/satellites",  # toutes les toutes qui commence par /satellites
    tags=["satelittes"]   # pour grouper la doc dans Swagger
)


def get_db():
    """
    Fournit une session DB et la ferme automatiquement aptès la requête
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[SatelliteSchema])
def get_satellites(db: Session = Depends(get_db)):
    """
    Retourne la liste de tous les satellites
    Args:
        db (Session, optional): _description_. Defaults to Depends(get_db).
    """
    satellites = db.execute(select(Satellite)).scalars().all()
    return satellites
