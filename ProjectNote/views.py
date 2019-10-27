from django.shortcuts import render
from ProjectNote.models import Note
from ProjectNote.form import NoteForm


def notes_list(request):
    all_notes = Note.objects.all()
    return render(request, "ProjectNote/notes_list.html", {
        "notes": all_notes,
    })


# pk = PrimaryKey
def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    items = note.items
    return render(request, "ProjectNote/notes_detail.html", {
        "note": note,
        "items": items,
    })


def notes_create(request):
    form = NoteForm()
    return render(request, "ProjectNote/notes_create.html", {"form": form})
