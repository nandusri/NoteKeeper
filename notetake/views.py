from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
	notes = Note.objects.all().order_by('-created_on')
	return render(request, 'notetake/note_list.html',{'notes':notes})
def note_detail(request,pk):
	note = get_object_or_404(Note, pk=pk)
	return render(request, 'notetake/note_detail.html', {'note': note})
def note_new(request):
	if request.method == "POST":
		form = NoteForm(request.POST)
		if form.is_valid():
			note = form.save(commit=False)
			note.user = request.user
			note.save()
			return redirect('note_detail', pk=note.pk)
	else:
		form = NoteForm()
	return render(request, 'notetake/note_edit.html', {'form': form})
def note_edit(request, pk):
	note = get_object_or_404(Note, pk=pk)
	if request.method == "POST":
		form = NoteForm(request.POST, instance=post)
		if form.is_valid():
			note = form.save(commit=False)
			note.user = request.user
			note.save()
			return redirect('note_detail', pk=note.pk)
	else:
		form = NoteForm(instance=post)
	return render(request, 'notetake/note_edit.html', {'form': form})	
		
