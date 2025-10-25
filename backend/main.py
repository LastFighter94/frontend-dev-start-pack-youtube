from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

# создаём приложение
app = FastAPI()

# разрешаем запросы от фронта (например, localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # или ["http://localhost:5173"] для точности
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items")
def get_items():
    items = [
        {
            "id": 1,
            "name": "Docker",
            "img": "https://cp.beget.com/shared/fY3dp6t0OwxL8qsMxzHhWANqgULHLa46/docker2x.png.webp",
        },
        {
            "id": 2,
            "name": "Nginx",
            "img": "https://www.svgrepo.com/show/373924/nginx.svg",
        },
        {
            "id": 3,
            "name": "GitHub",
            "img": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
        },
    ]
    random.shuffle(items)
    return items
