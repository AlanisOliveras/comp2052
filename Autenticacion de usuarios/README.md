# Mini Proyecto de Autenticación con Flask-Login

Este mini proyecto demuestra cómo implementar un sistema básico de autenticación de usuarios utilizando Flask y la extensión Flask-Login. Incluye inicio de sesión, manejo de sesiones, rutas protegidas y cierre de sesión.

---

## Características Principales

- Inicio de sesión de usuarios con verificación de credenciales (usando contraseñas en **hash**).
- Mantenimiento de sesiones utilizando Flask-Login.
- Protección de rutas usando `@login_required`.
- Cierre de sesión y manejo seguro de sesiones.
- Plantillas HTML simples para el login.

---

## Estructura del Proyecto
login_project/
|
|
|------ app.py
|------requirements.txt
|------ templates/
          |
          |---- login.html
          |
          |----- home.html

---

## Instalación y Ejecución
1. Clonar o descargar el proyecto:

```bash
git clone https://github.com/tu_usuario/ProyectoAutenticacion.git
cd ProyectoAutenticacion

## Instalar las dependencias
pip install -r requirements.txt

##Ejecutar la aplicación
python app.py

## Abrir el navegador en:
http://127.0.0.1:5000/login

## Usuario Disponibles (Base simulada)
 | Usario | Contraseña | Rol   |
 | ------ | ---------- | ------|
 | Daynna | Nala2014   | admin |
 | Javier | Vale1546   | user  |

 ## Tecnologías Utilizadas
 - **Python 3.8+**
 - **Flask 2.x**
 - **Flask-Login**

## Recursos Útiles
- **Documentación oficial de Flask
- **Flask-Login

 ## Posibles Extenciones
 - **Integracióon con una base de datos real 
 (SQLite PostgreSQL, etc.).**
 - **Registro de nuevos usuarios**
- **Implementación avanzada de roles y premios**







