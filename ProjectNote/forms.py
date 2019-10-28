from django import forms
from ProjectNote.models import Note, NoteItem


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']

class NoteItemForm(forms.ModelForm):
    class Meta:
        model = NoteItem
        fields = ['body']






    # title = forms.CharField(label="List Name", max_length=100)
    # description = forms.CharField(widget=forms.Textarea, required=False)
