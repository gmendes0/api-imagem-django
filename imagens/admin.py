from django.contrib import admin
from imagens.models import Image

# Register your models here.

class ListImages(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'foto', 'data')
    list_display_link = ('id', 'descricao')

admin.site.register(Image, ListImages)
