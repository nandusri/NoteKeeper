from django.shortcuts import render, get_object_or_404
from .models import Note

def note_list(request):
	notes = Note.objects.all().order_by('-created_on')
	return render(request, 'notetake/note_list.html',{'notes':notes})
def note_detail(request,pk):
	note = get_object_or_404(Note, pk=pk)
	return render(request, 'notetake/note_detail.html', {'note': note})
		
