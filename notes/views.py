from django.shortcuts import render, redirect
from .models import Note, TagData


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        listT = TagData.objects.all()
        print(listT)
        if not tag in listT:
            TagData.objects.create(tagTitle=tag)
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        Note.objects.create(title=title, content=content, tagContent=TagData.objects.get(tagTitle=tag))
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
        listT = TagData.objects.all()
        print(listT)
        if not tag in listT:
            TagData.objects.create(tagTitle=tag)
        if title != '':
            note.title = title
        if content != '':
            note.content = content
        if tag != '':
            note.tagContent = TagData.objects.get(tagTitle=tag)
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

def tagsDetalhadas(request, tagTitle):
    print(tagTitle)
    all_notes = Note.objects.all()
    tagsDet = []
    for note in all_notes:
        if str(note.tagContent) == str(tagTitle):
            tagsDet.append(note)
    return render(request, 'notes/tagsDetalhadas.html', {'tagsDetalhadas': tagsDet})
