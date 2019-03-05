from django.shortcuts import render
def note_list(request):
	return render(request, 'notetake/note_list.html',{})
	