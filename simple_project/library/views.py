from django.shortcuts import render
from .models import Item  # Import the Item model

def all_books_view(request):
    books = Item.objects.all()  # Retrieve all books
    return render(request, 'library/all_books.html', {'books': books})  # Pass books to the template

def books_by_author_view(request, author_name):
    books = Item.objects.filter(author=author_name)  # Filter books by author
    return render(request, 'library/books_by_author.html', {'books': books, 'author': author_name})
