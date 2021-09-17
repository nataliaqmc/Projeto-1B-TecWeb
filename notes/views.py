from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        Note.objects.create(title=title, content=content, tag=tag)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        id = request.POST.get('identificador')
        note = Note.objects.get(id=id)
        if title != '':
            note.title = title
        if content != '':
            note.content = content
        if tag != '':
            note.tag = tag
        note.save()
        return redirect('index')

def delete(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.delete()
    return redirect('index')
    