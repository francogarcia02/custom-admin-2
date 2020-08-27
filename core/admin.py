from django.contrib import admin
from core.models import *

###  1)     ----------------------------------------------------###
class LibroSup(admin.ModelAdmin):
    list_display = ['titulo', 'editorial']

###  2)     ----------------------------------------------------###
class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informacion Personal', {
            'fields': ('nombre','codigo')
        }),
        ('Contactos', {
            'fields': ('telefono','direccion')
        })
    )
###  3)     ----------------------------------------------------###
class LibrosAdmin(admin.ModelAdmin):
    list_filter = ('titulo',)

###  4)     ----------------------------------------------------###
class AutorInLine(admin.TabularInline):
    model = Autor
    extra = 2
class LibrossAdmin(admin.ModelAdmin):
    list_display = ('titulo','editorial')
    inlines = [AutorInLine]

###  5)     ----------------------------------------------------###
class AutorAdmin(admin.ModelAdmin):
    list_filter = ('nombre', 'matricula')


admin.site.register(Libros, LibroSup)
"""admin.site.register(Libros, LibrosAdmin)"""
"""admin.site.register(Libros, LibrossAdmin)"""
admin.site.register(Autor, AutorAdmin)
admin.site.register(Usuario, UsuarioAdmin)
