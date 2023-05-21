from django.http import HttpResponse
from django.conf import settings
import xlwt
from io import BytesIO
from datetime import date
from django.template.defaultfilters import yesno
from datetime import datetime


def exportar_simpatizantes(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = "attachment; filename=Simpatizantes.xls"

    wb = xlwt.Workbook()
    ws = wb.add_sheet("Simpatizantes")

    incremento = 1

    ws.write_merge(
        0,
        1,
        0,
        21,
        "Reporte Simpatizantes",
        xlwt.easyxf(
            "align: horiz center; font: bold on, height 350; pattern: pattern solid, fore_colour grey25; borders: left thin, right thin, top thin, bottom thin;"
        ),
    )

    ws.write(2, 0, "Id")
    ws.write(2, 1, "Fecha registro")
    ws.write(2, 2, "Candidato")
    ws.write(2, 3, "Cédula")
    ws.write(2, 4, "Estado")
    ws.write(2, 5, "Rol")
    ws.write(2, 6, "Referido Por")
    ws.write(2, 7, "Primer nombre")
    ws.write(2, 8, "Segundo nombre")
    ws.write(2, 9, "Primer Apellido")
    ws.write(2, 10, "Segundo Apellido")
    ws.write(2, 11, "Departamento")
    ws.write(2, 12, "Municipio")
    ws.write(2, 13, "Barrio / Comuna")
    ws.write(2, 14, "Dirección")
    ws.write(2, 15, "Teléfono principal")
    ws.write(2, 16, "Fecha nacimiento")
    ws.write(2, 17, "Puesto Votación")
    ws.write(2, 18, "Mesa Votación")
    ws.write(2, 19, "Observaciones")
    ws.write(2, 20, "Población")
    ws.write(2, 21, "Guardado por")

    counter = 4

    for obj in queryset:
        ws.write(counter, 0, obj.id)
        ws.write(counter, 1, obj.fecha_registro.strftime('%d/%m/%y'))
        ws.write(counter, 2, f"{obj.candidato.nombres} {obj.candidato.apellidos}")
        ws.write(counter, 3, obj.cedula)
        ws.write(counter, 4, obj.estado)
        ws.write(counter, 5, obj.rol.nombre)
        if obj.referido_por:
            ws.write(counter, 6, f"{obj.referido_por.primer_nombre} {obj.referido_por.primer_apellido}")
        else: 
            ws.write(counter, 6, "")
        ws.write(counter, 7, obj.primer_nombre)
        ws.write(counter, 8, obj.segundo_nombre)
        ws.write(counter, 9, obj.primer_apellido)
        ws.write(counter, 10, obj.segundo_apellido)
        ws.write(counter, 11, obj.departamento.nombre)
        ws.write(counter, 12, obj.municipio.nombre)
        ws.write(counter, 13, obj.barrio_comuna)
        ws.write(counter, 14, obj.direccion)
        ws.write(counter, 15, obj.telefono_principal)
        if obj.fecha_nacimiento:
            ws.write(counter, 16, obj.fecha_nacimiento.strftime('%d/%m/%y'))
        else:
            ws.write(counter, 16, "")
        ws.write(counter, 17, obj.puesto_votacion.nombre)
        ws.write(counter, 18, obj.mesa_votacion)
        ws.write(counter, 19, obj.observaciones)
        if obj.poblacion:
            ws.write(counter, 20, obj.poblacion.nombre)
        else:
            ws.write(counter, 20, "")
        ws.write(counter, 21, obj.guardado_por.username)

        counter = counter + incremento

    wb.save(response)
    return response


exportar_simpatizantes.short_description = "Exportar Simpatizantes"
