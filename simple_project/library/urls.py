# filepath: d:\Projects\Python\Django\simple_project\library\urls.py

from django.http import HttpResponseRedirect
from django.urls import path
from .views import all_books_view, books_by_author_view

def redirect_to_books(request):
    return HttpResponseRedirect('/library/books/')

urlpatterns = [
    path('', redirect_to_books),  # Redirect /library to /library/books/
    path('books/', all_books_view, name='all_books'),
    path('books/author/<str:author_name>/', books_by_author_view, name='books_by_author'),
]