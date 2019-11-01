from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    id =  models.IntegerField(primary_key=True)


class Pregunta(models.Model):
    descripcion = models.CharField(max_length=200)
    texto = models.CharField(max_length=200)

class Respuesta(models.Model):
	texto = models.CharField(max_length=200)
	pregunta= models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	aplausos = models.IntegerField()
