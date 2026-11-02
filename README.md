# ENGELSTRÄNEN - Proyecto Django

## Requisitos
- Python 3.10 o superior
- pip

## Instalación en macOS
Abre Terminal y entra a la carpeta del proyecto:

```bash
cd ruta/a/ENGELSTRANEN
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations usuarios
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre http://127.0.0.1:8000/

## Rutas
- `/` Página principal pública
- `/registro/` Registro (rol cliente automático)
- `/login/` Inicio de sesión
- `/logout/` Cierre de sesión (POST)
- `/perfil/` Perfil privado
- `/panel-admin/` Panel de administrador
- `/panel-productor/` Panel de productor
- `/admin/` Administración de Django

## Roles
El registro público siempre crea usuarios con rol `cliente`.
Para cambiar un usuario a `productor`, entra al administrador de Django con una cuenta superusuario y edita su campo Rol. Los superusuarios tienen rol administrador automáticamente.

## Nota
La base de datos SQLite se crea al ejecutar `migrate`. No se incluye una base de datos preexistente.
# ENGELSTRANEN-v1
