from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("profesores", views.profesores , name="profesores"),
    path("eliminar_curso/<int:id>", views.eliminar_curso , name="eliminar_curso"),
    path("editar_curso/<int:id>" , views.editar_curso , name="editar_curso"),
    path("login", views.login_request , name="Login"),
    path("register", views.register , name="register"),
    path("opiniones", views.opiniones , name="opiniones" ),
    path("creador", views.creador , name="creador")

]