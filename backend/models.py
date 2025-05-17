from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: int
    title: str
    year: int
    genre: Optional[str]
    rating: Optional[int]
    director: str
    duration: Optional[int]
    liked: bool = False
