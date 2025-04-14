from django.http import JsonResponse
from .models import Libro

def home(request):
    return JsonResponse({'message': 'Benvenuto nella pagina principale!'})

def list_books(request):
    books = Libro.objects.all().order_by('anno_edizione')
    books_data = [
        {
            'titolo': book.titolo,
            'anno_edizione': book.anno_edizione,
            'editore': {
                'ragione_sociale': book.editore.ragione_sociale,
                'indirizzo': book.editore.indirizzo,
                'telefono': book.editore.telefono,
            },
            'autore': {
                'nome': book.autore.nome,
                'cognome': book.autore.cognome,
            }
        }
        for book in books
    ]
    return JsonResponse({'books': books_data})