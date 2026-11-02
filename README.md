# 🍺 ENGELSTRÄNEN
### Plataforma web de cerveza artesanal colombiana

¡Bienvenido al proyecto **ENGELSTRÄNEN**!

Este proyecto busca crear una plataforma web dedicada al mundo de la cerveza artesanal colombiana, donde los usuarios podrán descubrir productores, conocer sus productos, consultar calificaciones y formar parte de una comunidad cervecera.

Este repositorio está abierto a los integrantes del equipo que quieran colaborar en el desarrollo, realizar mejoras, corregir errores o agregar nuevas funcionalidades.

¡Gracias por formar parte de ENGELSTRÄNEN! 🍻

---

## 📌 1. Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- Python 3.10 o superior.
- pip (administrador de paquetes de Python).
- Visual Studio Code (recomendado).
- Git (opcional, si deseas clonar el repositorio).

**Descargas:**

- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/downloads)

---

## 📥 2. ¿Cómo descargar el proyecto?

Puedes descargar ENGELSTRÄNEN directamente desde GitHub.

**Repositorio oficial:**

[https://github.com/dragones46/ENGELSTRANEN-v1](https://github.com/dragones46/ENGELSTRANEN-v1)

### Opción A: Descargar en Windows o macOS mediante ZIP

1. Entra al repositorio de GitHub.
2. Busca el botón verde llamado **Code**.
3. Haz clic en él.
4. Selecciona **Download ZIP**.
5. Espera a que termine la descarga.
6. Busca el archivo ZIP en la carpeta Descargas.
7. Haz clic derecho y selecciona **Extraer todo** en Windows o descomprime el archivo en macOS.
8. Abre la carpeta del proyecto con Visual Studio Code.

### Opción B: Descargar mediante Git

Si tienes Git instalado, abre una terminal y ejecuta:

```bash
git clone https://github.com/dragones46/ENGELSTRANEN-v1.git
```

Después entra en la carpeta:

```bash
cd ENGELSTRANEN-v1
```

---

## 🪟 3. Instalación en Windows

### Paso 1. Abrir el proyecto

Abre la carpeta del proyecto en Visual Studio Code.

En el menú superior selecciona:

**Terminal → New Terminal**

### Paso 2. Crear el entorno virtual

En la terminal ejecuta:

```powershell
python -m venv venv
```

Si el comando `python` no funciona, prueba:

```powershell
py -m venv venv
```

### Paso 3. Activar el entorno virtual

En PowerShell ejecuta:

```powershell
.\venv\Scripts\Activate.ps1
```

Si aparece un error relacionado con la política de ejecución, ejecuta primero:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Después vuelve a activar el entorno virtual.

**Si utilizas CMD en lugar de PowerShell**, ejecuta:

```cmd
venv\Scripts\activate.bat
```

Cuando esté activado, aparecerá `(venv)` al comienzo de la terminal.

### Paso 4. Instalar las dependencias

Ejecuta:

```bash
python -m pip install --upgrade pip
```

Después instala los paquetes:

```bash
pip install -r requirements.txt
```

### Paso 5. Preparar la base de datos

Ejecuta los siguientes comandos:

```bash
python manage.py makemigrations usuarios
python manage.py migrate
```

### Paso 6. Crear el administrador

Ejecuta:

```bash
python manage.py createsuperuser
```

Completa los datos que solicita Django para crear tu cuenta administradora.

### Paso 7. Iniciar el servidor

Ejecuta:

```bash
python manage.py runserver
```

Abre tu navegador en:

http://127.0.0.1:8000/

¡Ya puedes utilizar ENGELSTRÄNEN!

---

## 🍎 4. Instalación en macOS

### Paso 1. Abrir el proyecto

Abre la carpeta del proyecto en Visual Studio Code y abre una terminal.

### Paso 2. Crear el entorno virtual

```bash
python3 -m venv venv
```

### Paso 3. Activar el entorno virtual

```bash
source venv/bin/activate
```

### Paso 4. Instalar las dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Paso 5. Preparar la base de datos

```bash
python manage.py makemigrations usuarios
python manage.py migrate
```

### Paso 6. Crear el administrador

```bash
python manage.py createsuperuser
```

### Paso 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abre tu navegador en:

http://127.0.0.1:8000/

¡Listo! Ya tienes el proyecto funcionando en tu Mac.

---

## 🌐 5. Direcciones del proyecto

| Dirección | Funcionalidad |
|---|---|
| `/` | Página principal pública |
| `/registro/` | Registro de usuarios |
| `/login/` | Inicio de sesión |
| `/logout/` | Cerrar sesión |
| `/perfil/` | Perfil del usuario |
| `/panel-admin/` | Panel de administrador |
| `/panel-productor/` | Panel de productor |
| `/admin/` | Administración de Django |

---

## 👥 6. Sistema de roles

ENGELSTRÄNEN cuenta con tres roles principales:

**Cliente**
- Se asigna automáticamente al registrarse.
- Puede acceder a su perfil.
- No puede elegir su propio rol.

**Productor**
- Cuenta con un espacio exclusivo para productores.
- Su rol debe ser asignado por un administrador autorizado.

**Administrador**
- Tiene acceso al panel administrativo.
- Puede gestionar los usuarios y sus roles.
- Puede asignar el rol de productor.

Los superusuarios de Django tienen automáticamente el rol de administrador.

---

## 🗄️ 7. Base de datos

El proyecto utiliza SQLite como sistema de base de datos.

La base de datos se crea automáticamente al ejecutar:

```bash
python manage.py migrate
```

Cada integrante que descargue el proyecto debe crear su propia base de datos local.

**Importante:** no se incluye una base de datos con usuarios o contraseñas de otros integrantes.

---

## 🔄 8. ¿Cómo iniciar el proyecto en futuras ocasiones?

Una vez instalado, no necesitas repetir todo el proceso.

**En Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

**En macOS:**

```bash
source venv/bin/activate
python manage.py runserver
```

Para detener el servidor presiona:

`CTRL + C`

Para salir del entorno virtual ejecuta:

```bash
deactivate
```

---

## ⚠️ 9. Recomendaciones para trabajar en equipo

- Antes de modificar archivos, verifica que tengas la última versión del proyecto.
- No compartas contraseñas ni claves privadas.
- No subas tu carpeta `venv` al repositorio.
- No subas archivos de base de datos personales.
- Realiza pruebas antes de enviar cambios.
- Comunica al equipo los cambios realizados para evitar conflictos.

Si trabajas con Git, puedes actualizar tu copia local con:

```bash
git pull
```

---

## 💛 10. Agradecimientos

Gracias a todos los integrantes que participan en el desarrollo de **ENGELSTRÄNEN**.

Este proyecto representa el trabajo en equipo, el aprendizaje y el interés por desarrollar una plataforma que permita dar mayor visibilidad a la cerveza artesanal colombiana.

**¡Sigamos construyendo ENGELSTRÄNEN juntos!**

🍺 *ENGELSTRÄNEN — Cerveza artesanal colombiana.*
