# Jotta Strong Ecommerce - Django 🐍⚡

## Descripción del proyecto

Jotta Strong Ecommerce es una aplicación web desarrollada con Python y Django como proyecto final de portafolio Fullstack.

La plataforma permite gestionar la venta del Programa Strong Nivel Black mediante un flujo completo de ecommerce:

- Visualización de programas.
- Autenticación de usuarios.
- Catálogo conectado a base de datos.
- Carrito de compras.
- Confirmación de compra.
- Registro de órdenes.
- Administración de productos mediante Django Admin.

Además, cuenta con una landing page profesional orientada a nutrición deportiva, formulario de postulación y gestión de potenciales clientes.


---

# Vista previa del proyecto


## Home / Landing

![Home](static/img/capturas/home.png)


## Catálogo Ecommerce

![Catálogo](static/img/capturas/catalogo.png)


## Login Cliente

![Login](static/img/capturas/login.png)


## Carrito de compras

![Carrito](static/img/capturas/carrito.png)


## Compra confirmada

![Compra](static/img/capturas/compra.png)


## Administración de órdenes

![Ordenes](static/img/capturas/admin_ordenes.png)


## Administración de productos

![Productos](static/img/capturas/admin_productos.png)


---

# Funcionalidades implementadas

✔ Landing page responsive.

✔ Formulario de postulación conectado a base de datos.

✔ Validaciones de formulario.

✔ Login de usuarios.

✔ Gestión de roles mediante Django Auth.

✔ Catálogo dinámico desde base de datos.

✔ Administración de productos.

✔ Carrito de compras.

✔ Agregar y eliminar productos del carrito.

✔ Cálculo automático de subtotal y total.

✔ Confirmación de compra.

✔ Registro de órdenes asociadas al usuario.

✔ Panel administrador Django.


---

# Tecnologías utilizadas

- Python
- Django
- HTML5
- CSS3
- JavaScript
- SQLite
- Git / GitHub


---

# Arquitectura

El proyecto utiliza el patrón MVT de Django:

## Model

Gestión de modelos y base de datos mediante ORM.

Modelos principales:

### Postulante

- Nombre
- Correo
- Objetivo
- Experiencia
- Motivación
- Fecha registro


### Producto

- Nombre
- Descripción
- Precio
- Duración
- Incluye


### Orden

- Usuario
- Fecha
- Total


### ItemOrden

- Producto
- Cantidad
- Subtotal


---

# Instalación del proyecto

Clonar repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar al proyecto:

```bash
cd JottaStrong-Django
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Ejecutar servidor:

```bash
python manage.py runserver
```


---

# Rutas principales

Landing:

http://127.0.0.1:8000/

Catálogo:

http://127.0.0.1:8000/programas/

Carrito:

http://127.0.0.1:8000/carrito/

Login:

http://127.0.0.1:8000/login/

Administrador:

http://127.0.0.1:8000/admin/


---

# Usuarios de prueba


## Administrador

Usuario:

admin

Contraseña:

admin123


## Cliente

Usuario:

cliente

Contraseña:

cliente123


---

# Autora

Javiera Acevedo

Nutricionista deportiva y estudiante Fullstack Python/Django.

Proyecto que integra nutrición deportiva, tecnología y desarrollo web.