from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from db import engine


class Base(DeclarativeBase):
    pass
  

# User model
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    
    def  __repr__(self) -> str:
          return f"User(id={self.id}, name={self.name}, email={self.email})"   


# Create Tables

def create_tables():
   Base.metadata.create_all(engine)
   
# Delete Tables
def delete_tables():
    Base.metadata.drop_all(engine)