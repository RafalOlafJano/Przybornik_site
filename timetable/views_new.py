from django.shortcuts import render
from .models import TimeTable

# Create your views here.
def post_list_new(request):

    return render(request, 'timetable/wypelnienie.html', {})
