from django.shortcuts import render

from django.http import HttpResponse

from AppFamilia.models import Familiares

# Create your views here.


def familia(self):
        
    familiar_1= Familiares(nombre="Santiago", altura="180", fecha_nacimiento="1900-12-1")
    familiar_1.save()

    familiar_2= Familiares(nombre="Agustina", altura="160", fecha_nacimiento="1990-1-1")
    familiar_2.save()

    familiar_3= Familiares(nombre="Susana", altura="150", fecha_nacimiento="1980-10-1")
    familiar_3.save()

    texto= f"Mi familia se compone por 3 personas, mi hermano {familiar_1.nombre}, que mide {familiar_1.altura} y nacio en la fecha: {familiar_1.fecha_nacimiento}. Mi hermana {familiar_2.nombre}, que mide {familiar_2.altura} y nacio el dia {familiar_2.fecha_nacimiento} y mi mujer {familiar_3.nombre} que mide {familiar_3.altura} y nacio el {familiar_3.fecha_nacimiento}"


    return HttpResponse(texto)
