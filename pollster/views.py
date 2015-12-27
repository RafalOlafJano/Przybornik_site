from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import WypelnionaAnkieta
from django.utils import timezone

class PollForm(ModelForm):
    class Meta:
        model = WypelnionaAnkieta
        fields = ['odp1', 'odp2', 'odp3']

# Create your views here.
def post_list(request):

    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.author = request.user
            form.published_date = timezone.now()
            form.save()
        return redirect('wypelnienie.html')
    else:
        form = PollForm()

        return render(request, 'pollster/pollster.html', {'form': form})
