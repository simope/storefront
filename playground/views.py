from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db.models import Value, F
from store.models import Product, Collection, Cart, CartItem
from tags.models import TaggedItem

def say_hello(request):

    return render(request, 'hello.html', {'name':'Mosh'})