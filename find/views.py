from django.shortcuts import render
from django.utils import timezone

from note.models import Note

from guestbook.models import GBook

from pollster.models import WypelnionaAnkieta

from timetable.models import TimeTable



def post_list(request):

    return render(request, 'find/find.html', {})


def post_note(request):
    
    #notes = Note.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    notes = Note.objects.filter().order_by('published_date')
    # od najnowszej do najstarszej , order_by_desc 

    return render(request, 'find/find_note.html', {'notes' : notes})


def post_guestbook(request):

    guests = GBook.objects.filter().order_by('pierwsze_imie')
    # od najnowszej do najstarszej , order_by_desc 

    return render(request, 'find/find_guestbook.html', {'guests' : guests})


def post_pollster(request):

    polls = WypelnionaAnkieta.objects.filter().order_by('odp1')

    return render(request, 'find/find_pollster.html', {'polls' : polls})


def post_timetable(request):

    timetables = TimeTable.objects.filter().order_by('published_date')

    return render(request, 'find/find_timetable.html', {'timetables' : timetables})

