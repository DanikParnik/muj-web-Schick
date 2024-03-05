import random

from django.http import HttpResponse
from django.shortcuts import render


def loupak(request):
    random_number = random.randint(1,100)
    return (f"Random Number {random_number}")

def post_list(request):
    random_number = random.randint(1, 100)
    return render (request, 'blog/post_list.html', {"random_number":random_number})

# Create your views here.


