from fastapi import FastAPI, HTTPException, Depends
from models import Movie
from database import movies_db
from auth import decode_token, check_permission
from auth import create_token
from typing import List, Optional
from fastapi import Query

app = FastAPI()

@app.post("/token")
def login(role: Optional[str] = "VISITOR", permissions: Optional[List[str]] = Query(default=[])):
    jwt_data = {"role": role, "permissions": permissions}
    return {"access_token": create_token(jwt_data), "token_type": "bearer"}

# 🔓 GET is public
@app.get("/movies", response_model=List[Movie])
def get_movies(offset: int = 0, limit: int = 10):
    return movies_db[offset:offset+limit]

# 🔐 POST requires WRITE permission
@app.post("/movies", response_model=Movie)
def create_movie(movie: Movie, token=Depends(decode_token)):
    check_permission(token, "WRITE")
    movies_db.append(movie)
    return movie

# 🔐 PUT requires WRITE permission
@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, updated: Movie, token=Depends(decode_token)):
    check_permission(token, "WRITE")
    for idx, m in enumerate(movies_db):
        if m.id == movie_id:
            movies_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Movie not found")

# 🔐 DELETE requires WRITE permission
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, token=Depends(decode_token)):
    check_permission(token, "WRITE")
    for idx, m in enumerate(movies_db):
        if m.id == movie_id:
            return movies_db.pop(idx)
    raise HTTPException(status_code=404, detail="Movie not found")
