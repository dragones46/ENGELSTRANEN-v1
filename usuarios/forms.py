from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario


class RegistroForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = Usuario
        fields = [
            "username", "first_name", "last_name", "email",
            "fecha_nacimiento", "telefono", "direccion",
        ]
        labels = {
            "username": "Nombre de usuario",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "email": "Correo electrónico",
            "telefono": "Teléfono",
            "direccion": "Dirección",
        }

    def clean_fecha_nacimiento(self):
        nacimiento = self.cleaned_data["fecha_nacimiento"]
        hoy = date.today()
        edad = hoy.year - nacimiento.year - (
            (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)
        )
        if nacimiento > hoy:
            raise forms.ValidationError("La fecha de nacimiento no puede ser futura.")
        if edad < 18:
            raise forms.ValidationError(
                "Debes ser mayor de 18 años para registrarte en ENGELSTRÄNEN."
            )
        return nacimiento

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.rol = "cliente"
        if commit:
            usuario.save()
        return usuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs["class"] = "campo"


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs["class"] = "campo"

class ActualizarPerfilForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            "foto_perfil",
            "username",
            "email",
            "telefono",
            "direccion",
        ]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "campo",
                "placeholder": "Nombre de usuario"
            }),

            "email": forms.EmailInput(attrs={
                "class": "campo",
                "placeholder": "Correo electrónico"
            }),

            "telefono": forms.TextInput(attrs={
                "class": "campo",
                "placeholder": "Teléfono"
            }),

            "direccion": forms.TextInput(attrs={
                "class": "campo",
                "placeholder": "Dirección"
            }),

            "foto_perfil": forms.ClearableFileInput(attrs={
                "class": "campo",
                "accept": "image/*"
            }),
        }

    def clean_foto_perfil(self):
        foto = self.cleaned_data.get("foto_perfil")

        if foto and foto.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "La imagen no puede superar los 5 MB."
            )

        return foto