# models/user.py
# Esta clase representa la tabla de usuarios

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    """Docstring for user"""
    __tablename__ = "tbb_users"  # Corregido: un solo guión bajo y sin espacio
    
    id = Column(Integer, primary_key=True, index=True)
    rol_id = Column(Integer, ForeignKey("tbc_roles.id"))
    nombre = Column(String(60))
    p_apellido = Column(String(60))  # Corregido nombre del campo
    s_apellido = Column(String(60))  # Corregido nombre del campo
    usuario = Column(String(60))
    contraseña = Column(String(60))
    telefono = Column(String(60))
    status = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)
    
    # Relación con roles
    rol = relationship("Rol", back_populates="usuarios")