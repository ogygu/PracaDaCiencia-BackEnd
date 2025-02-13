from django.conf import settings
from django.db import models
from django.utils import timezone

'''
Tipo de Campo	
Campos de Texto	
	
CharField	Texto curto	models.CharField(max_length=100)
TextField	Texto longo	models.TextField()


Campos Numéricos		
IntegerField	Número inteiro	models.IntegerField()
PositiveIntegerField	Número inteiro positivo	models.PositiveIntegerField()
FloatField	Número decimal	models.FloatField()
DecimalField	Número decimal preciso	models.DecimalField(max_digits=5, decimal_places=2)


Campos de Data e Hora		
DateField	Apenas data	models.DateField()
DateTimeField	Data e hora	models.DateTimeField(auto_now_add=True)


Campos Booleanos		
BooleanField	Verdadeiro/Falso	models.BooleanField(default=True)

Campos de Relacionamento		
ForeignKey	Relação 1:N	models.ForeignKey("Author", on_delete=models.CASCADE)
OneToOneField	Relação 1:1	models.OneToOneField("User", on_delete=models.CASCADE)
ManyToManyField	Relação N:N	models.ManyToManyField("Course")

Campos Específicos		
EmailField	E-mail válido	models.EmailField(unique=True)
URLField	URLs	models.URLField()
SlugField	Slug (URLs amigáveis)	models.SlugField(unique=True)

'''
class Tecnico(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

