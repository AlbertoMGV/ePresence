from django.db import models

# Create your models here.

class Aula(models.Model):
    personas = models.IntegerField()
    #Estado= 0:verde 1:amarillo 2:rojo
    estado = models.IntegerField()
    hora_in = models.TimeField()
    hora_out = models.TimeField()
def __str__(self):
	return '%s %s %s %s' % (self.personas, self.estado, self.hora_out, self.hora_in)