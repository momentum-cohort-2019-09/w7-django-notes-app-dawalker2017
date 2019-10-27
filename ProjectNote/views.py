from django.shortcuts import render
from ProjectNote.models import Note


def notes_list(request):
    all_notes = Note.objects.all()
    return render(request, "ProjectNote/notes_list.html", {
        "notes": all_notes,
    })


# pk = PrimaryKey
def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    items = note.items.order_by('order')
    return render(request, "ProjectNote/notes_detail.html", {
        "note": note,
        "items": items,
        })
