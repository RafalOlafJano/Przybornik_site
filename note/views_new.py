from django.shortcuts import render
from .models import Note

# Create your views here.
def post_list_new(request):

    return render(request, 'note/wypelnienie.html', {})
