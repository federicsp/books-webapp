from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Libro
from django.views.decorators.csrf import csrf_exempt

import json


def home(request):
    return HttpResponse("Benvenuto nella pagina principale!")


def books_table(request):
    books = (
        Libro.objects.select_related("editore", "autore")
        .all()
        .order_by("anno_edizione")
    )

    # Imposta la pagina corrente dalla richiesta (default a 1)
    page_number = request.GET.get("page", 1)

    # Crea un paginator con 10 libri per pagina (puoi cambiare il numero)
    paginator = Paginator(books, 2)

    # Ottieni la pagina desiderata
    page_obj = paginator.get_page(page_number)

    # Passa la pagina dei libri al template
    return render(request, "books/table.html", {"page_obj": page_obj})


@csrf_exempt
def books(request):
    if request.method == "GET":
        books_list = (
            Libro.objects.all()
            .values("id", "titolo", "autore", "editore", "anno_edizione")
            .order_by("anno_edizione")
        )
        return JsonResponse(list(books_list), safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            if "libri" not in data or not isinstance(data["libri"], list):
                return JsonResponse(
                    {"error": "Invalid or missing 'libri' list"}, status=400
                )

            for lib in data["libri"]:
                if all(
                    k in lib for k in ("titolo", "autore", "editore", "anno_edizione")
                ):
                    Libro.objects.update_or_create(
                        titolo=lib["titolo"],
                        autore_id=lib["autore"],
                        editore_id=lib["editore"],
                        anno_edizione=lib["anno_edizione"],
                    )
                else:
                    return JsonResponse(
                        {"error": "Incomplete data in one or more entries"}, status=400
                    )

            return JsonResponse(
                {"message": f"{len(data['libri'])} books processed successfully!"}
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
