"""
Schema para usuarios del sistema de autolavado.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    """Base schema para usuarios."""
    nombre: constr(max_length=60)
    papellido: Optional[constr(max_length=60)] = None
    sapellido: Optional[constr(max_length=60)] = None
    direccion: Optional[constr(max_length=120)] = None
    telefono: Optional[constr(max_length=15)] = None
    correo: EmailStr
    username: constr(max_length=50)
    estatus: bool = True


class UserCreate(UserBase):
    """Schema para crear usuarios."""
    password: constr(min_length=6)


class UserUpdate(BaseModel):
    """Schema para actualizar usuarios."""
    nombre: Optional[constr(max_length=60)] = None
    papellido: Optional[constr(max_length=60)] = None
    sapellido: Optional[constr(max_length=60)] = None
    direccion: Optional[constr(max_length=120)] = None
    telefono: Optional[constr(max_length=15)] = None
    correo: Optional[EmailStr] = None
    username: Optional[constr(max_length=50)] = None
    estatus: Optional[bool] = None
    password: Optional[constr(min_length=6)] = None


class UserLogin(BaseModel):
    """Schema para inicio de sesión."""
    username: constr(max_length=50)
    password: str


class User(UserBase):
    """Schema completo para usuarios."""
    id: int
    rol_id: Optional[int] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None

    class Config:
        """Configuración de Pydantic."""
        orm_mode = True
