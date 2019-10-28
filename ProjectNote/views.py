from django.shortcuts import render, redirect, get_object_or_404
from ProjectNote.models import Note, NoteItem
from ProjectNote.forms import NoteForm, NoteItemForm


def notes_list(request):
    all_notes = Note.objects.all()
    return render(request, "ProjectNote/notes_list.html", {
        "notes": all_notes,
    })


# pk = PrimaryKey
def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == "POST":
        note_item_form = NoteItemForm(request.POST)
        if note_item_form.is_valid():
            new_item = note_item_form.save(commit=False)
            new_item.note = note

            last_item = note.items.order_by('-order')[0]
            new_item.order = last_item.order + 1

            new_item.save()

            return redirect(to='notes_detail', pk=pk)
    else:
        note_item_form = NoteItemForm()

    return render(request, "ProjectNote/notes_detail.html", {
        "item_form": note_item_form,
        "note": note,
    })

def notes_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_list')
    else:
        form = NoteForm()

    return render(request, "ProjectNote/notes_create.html", {"form": form})

def notes_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(request, 'ProjectNote/notes_edit.html', {
        "note": note,
        "form": form,
        })


