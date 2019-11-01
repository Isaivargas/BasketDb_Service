from django.db import models

# Create your models here.

class Datos_sensibles(models.Model):
	
	id = models.IntegerField()
	fechaModificacion = models.DateField()
	numeroSolicitud = models.IntegerField()

    id_objeto  = models.IntegerField(null=True)
    dato = models.CharField(max_legth=1000,null=True)



class Datos(models.Model):
    
    id = models.IntegerField()
    fechaModificacion = models.DateField()
    numeroSolicitud = models.IntegerField()

    id_objeto   = models.IntegerField(null=True)
    dato = models.CharField(max_legth=1000,null=True)

		


