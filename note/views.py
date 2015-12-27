from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Note

# Create your views here.
class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
		


def post_list(request):

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('wypelnienie.html')
    else:
        form = NoteForm()

    return render(request, 'note/note.html', {'form': form})