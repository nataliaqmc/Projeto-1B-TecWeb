from django.contrib import admin
from .models import Note, TagData


admin.site.register(Note)
admin.site.register(TagData)