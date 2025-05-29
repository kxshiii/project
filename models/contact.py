from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from contact_book_orm.models.base import Base

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=True)
    password_salt = Column(String(64), nullable=True)
    password_hash = Column(String(128), nullable=True)

    group = relationship("Group", back_populates="contacts")

    def __repr__(self):
        return (
            f"<Contact(id={self.id}, "
            f"name='{self.first_name} {self.last_name}', "
            f"email='{self.email}', "
            f"phone='{self.phone}', "
            f"group_id={self.group_id})>"
        )