from django.shortcuts import render
from .models import Project
# Create your views here.


def portfolio(request):
    # Extraemos de la bd todos los proyectos en una variable projects
    # y luego la inyectamos en el template con un diccionario
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects})