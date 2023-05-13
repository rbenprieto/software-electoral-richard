from django.contrib import admin
from .models import (
    Departamento,
    Municipio,
    PuestoVotacion,
    EnfoquePoblacional,
    Candidato,
    Rol,
    Simpatizante,
)


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
    )
    list_display_links = list_display


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "departamento")
    list_display_links = list_display


@admin.register(PuestoVotacion)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "direccion")
    list_display_links = list_display


@admin.register(EnfoquePoblacional)
class EnfoquePoblacionalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
    )
    list_display_links = list_display


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "apellidos", "tipo_campania", "is_active")
    list_display_links = list_display


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre",)
    list_display_links = list_display


@admin.register(Simpatizante)
class SimpatizanteAdmin(admin.ModelAdmin):
    list_display = ("id", "cedula", "primer_nombre", "primer_apellido", "rol", "candidato", "telefono_principal")
    list_display_links = list_display
    list_per_page = 30