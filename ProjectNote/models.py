from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NoteItem(models.Model):
    body = models.CharField(max_length=255)
    checklist = models.ForeignKey(
        to=Note, on_delete=models.CASCADE, related_name='items')
