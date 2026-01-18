import json

favourite = {
    "type": "movie",
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014,
    "genre": "Science Fiction",
    "duration_minutes": 169,
    "rating": 8.6
}

with open("favourite.json", "w", encoding="utf-8") as file:
    json.dump(favourite, file, ensure_ascii=False, indent=2)

print("Saved to favourite.json")