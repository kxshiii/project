from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from contact_book_orm.models.base import Base

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    contacts = relationship(
        "Contact",
        back_populates="group",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"<Group(id={self.id}, "
            f"name='{self.name}', "
            f"description='{self.description}')>"
        )