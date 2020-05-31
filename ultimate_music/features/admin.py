from django.contrib import admin
from .models import Song,Instrumental,Video

# Register your models here.
admin.site.register(Song)
admin.site.register(Instrumental)
admin.site.register(Video)