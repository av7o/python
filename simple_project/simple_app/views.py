from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required  # Import the decorator
from .models import Item

# Create your views here.

def hello_view(request):
    return HttpResponse("გამარჯობა, Django!")

def about_view(request):
    return HttpResponse("ეს არის ტესტ აპლიკაცია")

@login_required  # Protect the view with login_required
def secure_view(request):
    return HttpResponse("This is a secure page. You must be logged in to view it.")

def item_detail_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Retrieve the item by ID or return 404
    return render(request, 'simple_app/item_detail.html', {'item': item})  # Render the template

def home_view(request):
    return HttpResponse("ეს არის მთავარი გვერდი")
