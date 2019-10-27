from django.contrib import admin
from ProjectNote.models import Note, NoteItem


class NoteItemInline(admin.StackedInline):
    model = NoteItem
    extra = 0


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'item_count',
        'created_at',
        'updated_at'
    )

    inlines = [NoteItemInline]


admin.site.register(Note, NoteAdmin)
admin.site.register(NoteItem)
