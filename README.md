# Prueba Python - Abaqus

Este proyecto corresponde a una aplicación desarrollada en **Django** para procesar información proveniente de un archivo **Excel (.xlsx)** y visualizar los resultados mediante una interfaz web.

## Requisitos

Antes de comenzar, asegúrate de tener instalado:

* Python 3.10 o superior
* pip
* Git (opcional, para clonar el repositorio)

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/AndresBC11/PruebaPython-Abaqus.git
cd PruebaPython-Abaqus
```

Se recomienda crear y activar un entorno virtual.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Configuración de la base de datos

Ejecuta las migraciones para crear la estructura de la base de datos:

```bash
python manage.py migrate
```
(En caso de error en el paso siguiente puedes eliminar la base de datos con "del db.sqlite3" y lanzar migrate de nuevo)

## Carga del archivo Excel

Una vez creada la base de datos, carga el archivo `.xlsx` utilizando el comando correspondiente del proyecto.

```bash
python manage.py importar_xlsx <ruta archivo.xlsx>
```

**Ejemplo:**

```bash
python manage.py importar_xlsx datos.xlsx
```

> Reemplaza `datos.xlsx` por la ruta del archivo que deseas importar.

## Ejecutar el servidor

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Por defecto, la aplicación estará disponible en:

```
http://127.0.0.1:8000/
```
Al entrar serás redigirido a una URL con fechas de inicio/fin y un portafolio por defecto. El rango de fechas es [15-02-2022,16-02-2023], con opción de "Portafolio 1" y "Portafolio 2"

## API
La API se encuentra en 
localhost:8000/api/pesos-activos/?fecha_inicio=1900-01-01&fecha_fin=2100-02-17&portafolio=Portafolio 1 
localhost:8000/api/valor-historico/?fecha_inicio=1900-01-01&fecha_fin=2100-02-17&portafolio=Portafolio 1 
con fechas y portafolios editables por supuesto.

## Flujo de ejecución

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar las dependencias.
4. Ejecutar las migraciones.
5. Cargar el archivo `.xlsx`.
6. Iniciar el servidor de desarrollo.

## Estructura general

```
.
├── manage.py
├── requirements.txt
├── db.sqlite3
├── portafolio/
├── templates/
├── static/
└── ...
```
