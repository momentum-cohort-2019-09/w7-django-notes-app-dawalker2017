from django.db import models


class Note(models.Model):
    title = models.CharField(
        verbose_name="Note Title:",
        max_length=100,
        help_text="Max Characters: 100")
    description = models.TextField(
        verbose_name="Note Description:",
        max_length=255,
        help_text="Max Characters: 255",
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def item_count(self):
        return self.items.count()

    def __str__(self):
        return self.title


class NoteItem(models.Model):
    body = models.CharField(
        max_length=255,
        help_text="Max Characters: 255",
    )
    checklist = models.ForeignKey(
        to=Note, on_delete=models.CASCADE, related_name='items')

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
