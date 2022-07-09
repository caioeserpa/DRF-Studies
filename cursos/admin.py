from csv import list_dialects
from django.contrib import admin

from .models import Curso, Avaliacao
# Register your models here.
@admin.register

class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo","url","criacao","atualizacao","ativo")

@admin.register(Avaliacao)
class AavaliacaoAdmin(admin.ModelAdmin):
    list_display = ("curso", "nome", "email", "avaliacao", "criacao", "atualizacao", "ativo")


