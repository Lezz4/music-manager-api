# db/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    album_id = Column(Integer, ForeignKey("albums.id"))
    year = Column(Integer, nullable=False)

    artist = relationship("Artist", back_populates="songs")
    album = relationship("Album", back_populates="songs")


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    songs = relationship("Song", back_populates="artist")


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id"))

    artist = relationship("Artist")
    songs = relationship("Song", back_populates="album")
