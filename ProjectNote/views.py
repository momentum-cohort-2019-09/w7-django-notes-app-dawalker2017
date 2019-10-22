from django.shortcuts import render

# Create your views here.


def notes_list(request):
    return render(reqeust, "ProjectNote/templates/notes_list.html", {
        "list": NOTES,
    })


def notes_detail(request, id):
    note_id = NOTES[id]
    return render(request. "ProjectNote/templated/notes_list.html", {"note_id": note_id})
