import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, func
from sqlalchemy.orm import relationship
from config.database import Base

class UserType(enum.Enum):
    franchisor = "Franchisor"
    buyer = "Buyer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    user_type = Column(Enum(UserType), nullable=False)
    is_otp_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    franchisor = relationship("Franchisor", back_populates="user")
    buyer = relationship("Buyer", back_populates="user")
