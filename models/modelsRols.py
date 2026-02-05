# models/rol.py
# Esta clase representa la tabla de roles de usuarios

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    """En este apartado se define la clase con sus atributos"""
    __tablename__ = "tbc_roles"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(60))
    estatus = Column(Boolean)
    
    # Relación con usuarios
    usuarios = relationship("User", back_populates="rol")