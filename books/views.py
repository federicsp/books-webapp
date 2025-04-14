from django.http import HttpResponse
from .models import Libro
from django.shortcuts import render


def home(request):
    return HttpResponse('Benvenuto nella pagina principale!')

def books_table(request):
    books = Libro.objects.select_related('editore', 'autore').all().order_by('anno_edizione')
    return render(request, 'books/table.html', {'books': books})
