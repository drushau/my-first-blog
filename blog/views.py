from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#inicio
def index(request):
    plantilla=loader.get_template("pagina.html")
    contexto={
        'titulo':'Inicio'
    }
    return HttpResponse(plantilla.render(contexto,request))

#noticias
def noticias(request):
    plantilla=loader.get_template("noticias.html")
    contexto={
        'noticias':noticias
    }

    return HttpResponse(plantilla.render(contexto))

def formulario(request):
    plantilla=loader.get_template("formulario.html")
    contexto={
        'formulario':formulario
    }
    return HttpResponse(plantilla.render(contexto))

def eventos(request):
    
    plantilla=loader.get_template("eventos.html")
    contexto={
        'eventos':eventos
    }
    return HttpResponse(plantilla.render(contexto))

def about(request):
    plantilla=loader.get_template("about.html")
    contexto={
        'about':about
    }
    return HttpResponse(plantilla.render(contexto))