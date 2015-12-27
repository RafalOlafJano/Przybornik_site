from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import GBook

# Create your views here.



# Create your views here.
class GBookForm(ModelForm):
    class Meta:
        model = GBook
        fields = ['pierwsze_imie', 'drugie_imie', 'nazwisko', 'zawód', 'email', 'text']
		


def post_list(request):

    if request.method == 'POST':
        form = GBookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('wypelnienie.html')
    else:
        form = GBookForm()

    return render(request, 'guestbook/guestbook.html', {'form': form})