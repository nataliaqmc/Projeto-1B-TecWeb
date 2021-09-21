from django.shortcuts import render, redirect
from .models import Note, TagData


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        Note.objects.create(title=title, content=content, tagContent=tag)
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
            note.tagContent = tag
        note.save()
        return redirect('index')

def delete(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.delete()
    return redirect('index')
    
def tags(request):
    if request.method == 'POST':
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        
        TagData.objects.create()
        return redirect('index')
    else:
        all_tags = TagData.objects.all()
        print(all_tags[0])
        return render(request, 'notes/tags.html', {'tags': all_tags})
