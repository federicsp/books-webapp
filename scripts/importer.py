import json
from books.models import Libro, Autore, Editore
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books_webapp.settings")
django.setup()

with open("scripts/db.json") as f:
    data = json.load(f)

for e in data["editori"]:
    e = {k.replace(" ", "_"): v for k, v in e.items()}
    Editore.objects.update_or_create(id=e["id"], defaults=e)

for a in data["autori"]:
    a = {k.replace(" ", "_"): v for k, v in a.items()}
    Autore.objects.update_or_create(id=a["id"], defaults=a)

for lib in data["libri"]:
    lib = {k.replace(" ", "_"): v for k, v in lib.items()}
    Libro.objects.update_or_create(
        titolo=lib["titolo"],
        autore_id=lib["autore"],
        editore_id=lib["editore"],
        anno_edizione=lib["anno_edizione"],
    )
