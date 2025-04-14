from django.http import HttpResponse
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

