import json
from books.models import Libro, Autore, Editore
import os, django, json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_webapp.settings')
django.setup()

with open("scripts/db.json") as f:
    data = json.load(f)

for e in data["editori"]:
    Editore.objects.update_or_create(id=e["id"], defaults=e)

for a in data["autori"]:
    Autore.objects.update_or_create(id=a["id"], defaults=a)

for l in data["libri"]:
    Libro.objects.create(
        titolo=l["titolo"],
        autore_id=l["autore"],
        editore_id=l["editore"],
        anno_edizione=l["anno_edizione"]
    )
