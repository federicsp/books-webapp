from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Libro

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

# Aggiungi un libro
def add_book(request):
    if request.method == 'POST':
        titolo = request.POST.get('titolo')
        autore = request.POST.get('autore')
        editore = request.POST.get('editore')
        anno_edizione = request.POST.get('anno_edizione')

        if titolo and autore and editore and anno_edizione:
            Libro.objects.create(
                titolo=titolo,
                autore=autore,
                editore=editore,
                anno_edizione=anno_edizione
            )
            return HttpResponse('Libro aggiunto con successo!')  # Successo
        else:
            return HttpResponse('Dati incompleti. Per favore, completa tutti i campi.', status=400)  # Errore
    return HttpResponseNotAllowed(['POST'])

# Vista per ottenere tutti i libri in formato JSON
def books(request):
    books_list = Libro.objects.all().values('id', 'titolo', 'autore', 'editore', 'anno_edizione').order_by('anno_edizione')
    return JsonResponse(list(books_list), safe=False)