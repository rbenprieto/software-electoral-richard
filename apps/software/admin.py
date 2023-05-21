from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (
    Departamento,
    Municipio,
    PuestoVotacion,
    EnfoquePoblacional,
    Candidato,
    Rol,
    Simpatizante,
)

from .actions import *

@admin.register(Departamento)
class DepartamentoAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "nombre",
    )
    list_display_links = list_display


@admin.register(Municipio)
class MunicipioAdmin(ImportExportModelAdmin):
    list_display = ("id", "nombre", "departamento")
    list_display_links = list_display


@admin.register(PuestoVotacion)
class MunicipioAdmin(ImportExportModelAdmin):
    list_display = ("id", "nombre", "direccion")
    list_display_links = list_display


@admin.register(EnfoquePoblacional)
class EnfoquePoblacionalAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "nombre",
    )
    list_display_links = list_display


@admin.register(Candidato)
class CandidatoAdmin(ImportExportModelAdmin):
    list_display = ("id", "nombres", "apellidos", "tipo_campania", "is_active")
    list_display_links = list_display


@admin.register(Rol)
class RolAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "nombre",
    )
    list_display_links = list_display


@admin.register(Simpatizante)
class SimpatizanteAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "cedula",
        "primer_nombre",
        "primer_apellido",
        "rol",
        "candidato",
        "telefono_principal",
    )
    list_display_links = list_display
    exclude = ("guardado_por",)
    actions = [exportar_simpatizantes]
    list_per_page = 30

    def save_model(self, request, obj, form, change):
        obj.guardado_por = request.user
        super().save_model(request, obj, form, change)
