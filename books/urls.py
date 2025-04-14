from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/table/', views.books_table, name='books_table'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/', views.books, name='books'),
]
