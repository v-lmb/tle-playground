from pydantic import BaseModel
from datetime import datetime


class SatelliteSchema(BaseModel):
    id: int
    name: str
    line1: str
    line2: str
    updated_at: datetime
    norad_id: int | None  # None car nullable de base

    class Config:
        from_attributes = True  # permet de lire un objet SQLAlchemy directement
