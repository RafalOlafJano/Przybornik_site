from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import TimeTable


# Create your views here.
class TimeTableForm(ModelForm):
    class Meta:
        model = TimeTable
        fields = ['day','month','year','hour','minute','text']


def post_list(request):

    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('wypelnienie.html')
    else:
        form = TimeTableForm()

        return render(request, 'timetable/timetable.html', {'form': form})


def post_list_new(request):

    return render(request, 'timetable/wypelnienie.html', {})