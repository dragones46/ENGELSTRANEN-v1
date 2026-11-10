from functools import wraps
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from .forms import *


def rol_requerido(*roles):
    def decorador(vista):
        @wraps(vista)
        @login_required
        def envoltura(request, *args, **kwargs):
            if request.user.is_superuser or request.user.rol in roles:
                return vista(request, *args, **kwargs)
            raise PermissionDenied
        return envoltura
    return decorador


class IniciarSesionView(LoginView):
    template_name = "usuarios/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True


def inicio(request):
    return render(request, "usuarios/inicio.html")


def registro(request):
    if request.user.is_authenticated:
        return redirect("inicio")
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f"¡Bienvenido a ENGELSTRÄNEN, {usuario.first_name or usuario.username}!")
            return redirect("inicio")
    else:
        form = RegistroForm()
    return render(request, "usuarios/registro.html", {"form": form})


@login_required
def perfil(request):
    return render(request, "usuarios/perfil.html")


@rol_requerido("admin")
def panel_admin(request):
    return render(request, "usuarios/panel_admin.html")


@rol_requerido("productor", "admin")
def panel_productor(request):
    return render(request, "usuarios/panel_productor.html")



@login_required
def actualizar_perfil(request):

    if request.method == "POST":
        form = ActualizarPerfilForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "¡Tu perfil se actualizó correctamente!"
            )

            return redirect("perfil")

    else:
        form = ActualizarPerfilForm(instance=request.user)

    return render(
        request,
        "usuarios/actualizar_perfil.html",
        {"form": form}
    )
