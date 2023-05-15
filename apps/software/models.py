from django.db import models

tipo_campaña_choices = (
    ("Edil", "Edil"),
    ("Concejo", "Concejo"),
    ("Alcaldia", "Alcaldia"),
    ("Asamblea", "Asamblea"),
    ("Gobernación", "Gobernación"),
)


class Departamento(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"


class Municipio(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"


class PuestoVotacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.nombre)

    class Meta:
        verbose_name = "Puesto Votación"
        verbose_name_plural = "Puestos Votación"


class EnfoquePoblacional(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Enfoque Poblacional"
        verbose_name_plural = "Enfoques Poblacionales"


class Candidato(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    tipo_campania = models.CharField(
        max_length=20, choices=tipo_campaña_choices, verbose_name="Tipo de campaña"
    )
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(
        Municipio, on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"


class Rol(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"


class Simpatizante(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    referido_por = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    barrio_comuna = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono_principal = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    puesto_votacion = models.ForeignKey(PuestoVotacion, on_delete=models.CASCADE)
    mesa_votacion = models.CharField(max_length=20)
    observaciones = models.TextField(null=True, blank=True)
    poblacion = models.ForeignKey(
        EnfoquePoblacional, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} {self.cedula}"

    class Meta:
        verbose_name = "Simpatizante"
        verbose_name_plural = "Simpatizantes"
        unique_together = (
            "cedula",
            "candidato",
        )
