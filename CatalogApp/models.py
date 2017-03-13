from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, primary_key=True)

    @property
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id
        }


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    description = Column(String(2000))
    category_name = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    created_at = Column(DateTime, default=datetime.datetime.now())
    __table_args__ = (ForeignKeyConstraint([category_name], [Category.name]), {})

    @property
    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
            "creator_id": self.user_id,
            "id": self.id,
            "category": self.category_name
        }


if __name__ == "__main__":
    engine = create_engine('postgresql+psycopg2://catalog:123@localhost/catalog')
    Base.metadata.create_all(engine)
