from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone

# Base -> Classe parente de tous les modèles
# SQLAlchemy l'utilise pour garder la liste de toutes les tables


class Base(DeclarativeBase):
    pass


class Satellite(Base):
    __tablename__ = "satellites"

    # Colonnes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    line1 = Column(String(100), nullable=False)
    line2 = Column(String(100), nullable=False)
    update_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Représentation lisible pour le debug
    def __repr__(self):
        return f"<Sattelite name={self.name}>"
