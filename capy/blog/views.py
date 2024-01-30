import random

from django.http import HttpResponse

def loupak(request):
    random_number = random.randint(1,100)
    return HttpResponse(f"Random Number {random_number}")

# Create your views here.


