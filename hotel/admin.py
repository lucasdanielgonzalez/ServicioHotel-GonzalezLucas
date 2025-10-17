from django.contrib import admin
from .models import Huesped

@admin.register(Huesped)
class HuespedAdmin(admin.ModelAdmin):
   
    list_display = ('id', 'apellido', 'nombre', 'dni', 'email','fecha_de_nacimiento')
    list_display_links = ('nombre', 'apellido')
    search_fields = ('dni',)
    list_filter = ('fecha_de_nacimiento',)
    ordering = ('apellido','nombre','dni')


