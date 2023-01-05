import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Seguidores(Base):
    __tablename__ = 'seguidores'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('usuarios.id'))
    user_to_id = Column(Integer, ForeignKey('usuarios.id'))
    
class Comentarios(Base):
    __tablename__ = 'comentarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comentarios_text = Column(String(250), nullable=False)
    autor_id = Column(Integer, ForeignKey('usuarios.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    
    #person = relationship(Person)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuarios.id'))

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    tipo = Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
