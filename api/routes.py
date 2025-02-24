# api/routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Mock database
music_db = []

# Pydantic model for music items
class Song(BaseModel):
    id: int
    title: str
    artist: str
    album: str
    year: int
# Create a new song
@router.post("/songs/", response_model=Song)
def create_song(song: Song):
    music_db.append(song)
    return song

# Read all songs
@router.get("/songs/", response_model=List[Song])
def get_songs():
    return music_db

# Read a single song by ID
@router.get("/songs/{song_id}", response_model=Song)
def get_song(song_id: int):
    for song in music_db:
        if song.id == song_id:
            return song
    raise HTTPException(status_code=404, detail="Song not found")

# Update a song
@router.put("/songs/{song_id}", response_model=Song)
def update_song(song_id: int, updated_song: Song):
    for index, song in enumerate(music_db):
        if song.id == song_id:
            music_db[index] = updated_song
            return updated_song
    raise HTTPException(status_code=404, detail="Song not found")

# Delete a song
@router.delete("/songs/{song_id}")
def delete_song(song_id: int):
    for index, song in enumerate(music_db):
        if song.id == song_id:
            del music_db[index]
            return {"message": "Song deleted successfully"}
    raise HTTPException(status_code=404, detail="Song not found")
