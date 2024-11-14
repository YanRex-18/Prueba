from django.db import models

class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_departamento


class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=100)
    descripcion = models.TextField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='cargos')

    def __str__(self):
        return self.nombre_cargo


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    fecha_contratacion = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='empleados')

    def __str__(self):
        return self.nombre


class Contrato(models.Model):
    TIPO_CONTRATO_CHOICES = [
        ('temporal', 'Temporal'),
        ('indefinido', 'Indefinido'),
    ]
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('finalizado', 'Finalizado'),
    ]
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='contratos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    tipo_contrato = models.CharField(max_length=10, choices=TIPO_CONTRATO_CHOICES)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"Contrato {self.id} - {self.empleado.nombre}"


class Asistencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='asistencias')
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Asistencia {self.fecha} - {self.empleado.nombre}"

    

    