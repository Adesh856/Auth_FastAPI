from sqlalchemy import Column, ForeignKey, Integer, String,Enum,Boolean
from sqlalchemy.orm import relationship
from .db.database import Base

class User(Base):
    """
    User model representing users in the database.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    full_name = Column(String(255),default=None)
    password = Column(String(255))
    role = Column(Enum("subaccount", "user", "admin", name="role_enum"), default="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.user_name}, email={self.email})>"
