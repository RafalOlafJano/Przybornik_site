from django.shortcuts import render
from .models import GBook

# Create your views here.
def post_list_new(request):

    return render(request, 'guestbook/wypelnienie.html', {})
