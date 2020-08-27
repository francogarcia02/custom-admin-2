from django.db import models


class Libros(models.Model):
    titulo= models.CharField(max_length=50)
    codigo= models.IntegerField(null=True)
    editorial= models.CharField(max_length=50, null=True)
    CantPags= models.IntegerField(null=True)
    CantCopias= models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    Libros = models.ForeignKey(Libros, null=True, blank=True, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    matricula= models.CharField(max_length=50)


    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length = 50, default = "nombre..")
    direccion = models.CharField(max_length = 50, default = "direccion..")
    codigo = models.IntegerField(default = 0)
    telefono = models.IntegerField(default= 0)

    def __str__(self):
        return self.nombre