from django.shortcuts import render
from .models import WypelnionaAnkieta

# Create your views here.
def post_list_new(request):

    return render(request, 'pollster/wypelnienie.html', {})
