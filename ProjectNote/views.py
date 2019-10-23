from django.shortcuts import render
from ProjectNote.models import Note


def notes_list(request):
    all_notes = Note.objects.all()
    return render(request, "ProjectNote/notes_list.html", {
        "notes": all_notes,
    })


# def notes_detail(request, id):
#     note = Note.objects.get(id=id)
#     return render(request, "ProjectNote/notes_detail.html", {"note": note})
