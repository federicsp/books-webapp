from django.http import JsonResponse
from .models import Libro

def home(request):
    return JsonResponse({'message': 'Benvenuto nella pagina principale!'})

def list_books(request):
    books = Libro.objects.all().order_by('anno_edizione')
    books_data = [
        {'titolo': book.titolo, 'anno_edizione': book.anno_edizione}
        for book in books
    ]
    return JsonResponse({'books': books_data})