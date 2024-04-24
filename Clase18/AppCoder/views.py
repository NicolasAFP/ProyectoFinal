from django.shortcuts import render, redirect
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import OpinionForm
from .models import Opinion

# Create your views here.


def inicio(request):
    return render( request , "padre.html")



def alta_curso(request,nombre):
    curso = Curso(nombre=nombre, camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)



def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alumnos(request):
    return render(request, "alumnos.html")



def curso_formulario(request):
    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")

    return render(request , "formulario.html")


def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

def profesores(request):
    return render(request, "profesores.html")


def eliminar_curso(request , id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()
    return render(request , "cursos.html" , {"cursos":curso})


def editar_curso(request , id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save() 

            return render(request , "cursos.html" , {"cursos":curso})

    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "Camada":curso.camada})
        
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user )
                return render( request, "inicio.html" , {"mensaje":f"Bienvenido/a {usuario}"})
            else:
                return HttpResponse(f"usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})



def opiniones(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opiniones')  
    else:
        form = OpinionForm()
    
    opiniones = Opinion.objects.all()  
    return render(request, 'opiniones.html', {'form': form, 'opiniones': opiniones})

def creador(request):
    return render(request, 'creador.html')