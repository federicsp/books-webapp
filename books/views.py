from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Libro

import json

def home(request):
    return HttpResponse('Benvenuto nella pagina principale!')

def books_table(request):
    books = Libro.objects.select_related('editore', 'autore').all().order_by('anno_edizione')

    # Imposta la pagina corrente dalla richiesta (default a 1)
    page_number = request.GET.get('page', 1)

    # Crea un paginator con 10 libri per pagina (puoi cambiare il numero)
    paginator = Paginator(books, 10)

    # Ottieni la pagina desiderata
    page_obj = paginator.get_page(page_number)

    # Passa la pagina dei libri al template
    return render(request, 'books/table.html', {'page_obj': page_obj})

def books(request):
    if request.method == 'GET':
        books_list = Libro.objects.all().values('id', 'titolo', 'autore', 'editore', 'anno_edizione').order_by('anno_edizione')
        return JsonResponse(list(books_list), safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            if not isinstance(data, list):
                return JsonResponse({'error': 'Deve essere una lista di libri'}, status=400)

            books = []
            for item in data:
                if all(k in item for k in ('titolo', 'autore', 'editore', 'anno_edizione')):
                    books.append(Libro(**item))
                else:
                    return JsonResponse({'error': 'Dati incompleti in un libro'}, status=400)

            Libro.objects.bulk_create(books)
            return JsonResponse({'message': f'{len(books)} libri aggiunti con successo!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return HttpResponseNotAllowed(['GET', 'POST'])