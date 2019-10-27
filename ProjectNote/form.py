from django import forms


class NoteForm(forms.Form):
    title = forms.CharField(label="List Name", max_length=100)
    description = forms.CharField(widget=forms.Textarea)
