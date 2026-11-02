from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("login/", views.IniciarSesionView.as_view(), name="login"),
    path("registro/", views.registro, name="registro"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("perfil/", views.perfil, name="perfil"),
    path("panel-admin/", views.panel_admin, name="panel_admin"),
    path("panel-productor/", views.panel_productor, name="panel_productor"),
]
