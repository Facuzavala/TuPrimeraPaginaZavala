from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    clave = models.CharField(max_length=15)
    documento = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Clave: {self.clave}, Documento: {self.documento}"

class Socios(models.Model):
    nro_socio = models.IntegerField()
    clave = models.CharField(max_length=15)

    def __str__(self):
        return f"Nro socio: {self.nro_socio}, Clave: {self.clave}"
    
class Entradas(models.Model):
    partido = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Partido: {self.partido}, Ubicacion: {self.ubicacion}, Valor Entrada: {self.valor}"