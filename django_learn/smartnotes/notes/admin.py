from django.contrib import admin
from .models import Note


# Register your models here.
@admin.register(Note)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']

    def __str__(self):
        return self.title
