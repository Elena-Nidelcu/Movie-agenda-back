from fastapi import FastAPI, HTTPException
from models import Movie
from database import movies_db
from typing import List

app = FastAPI()

@app.get("/movies", response_model=List[Movie])
def get_movies(skip: int = 0, limit: int = 10):
    return movies_db[skip:skip+limit]

@app.post("/movies", response_model=Movie)
def create_movie(movie: Movie):
    movies_db.append(movie)
    return movie

@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, updated: Movie):
    for idx, m in enumerate(movies_db):
        if m.id == movie_id:
            movies_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Movie not found")

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for idx, m in enumerate(movies_db):
        if m.id == movie_id:
            return movies_db.pop(idx)
    raise HTTPException(status_code=404, detail="Movie not found")
