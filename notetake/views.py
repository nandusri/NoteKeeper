from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

@login_required
def note_list(request):
	notes = Note.objects.all().order_by('-created_on')
	return render(request, 'notetake/note_list.html',{'notes':notes})
@login_required
def note_detail(request,pk):
	note = get_object_or_404(Note, pk=pk)
	return render(request, 'notetake/note_detail.html', {'note': note})
@login_required
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
@login_required
def note_edit(request, pk):
	note = get_object_or_404(Note, pk=pk)
	if request.method == "POST":
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			note = form.save(commit=False)
			note.user = request.user
			note.save()
			return redirect('note_detail', pk=note.pk)
	else:
		form = NoteForm(instance=note)
	return render(request, 'notetake/note_edit.html', {'form': form})	
@login_required
def note_delete(request, pk):
	note = get_object_or_404(Note, pk=pk)
	note.delete()
	return redirect('note_list')
def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('note_list')
	else:
		form = UserCreationForm()			
	context = {'form' : form}	
	return render(request, 'registration/register.html', context)
