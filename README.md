# Web_Program
First attemp to introduce ourselves to web development

## Diagrama de Modelos del Proyecto

![Diagrama de Modelos](Modelos.svg)


## Ejecución Local
### Dependencias
Instalar Dependencias
```
apt install python3 python3-pip3
pip3 install Django
pip3 install django-crispy-forms
```
### Ejecución
```
python3 manage.py runserver 0.0.0.0:8000
```

## Docker
### Creación de la Imagen con Docker
Para crear una imagen con todo lo requerido para ejecutar el proyecto, correr:
```
docker build . --file Dockerfile --tag proyecto2
```

### Creación de un Contenedor a Partir de la Imagen Creada
Para iniciar el contenedor a partir de la imagen creada y acceder a la terminal,
correr:
```
docker run -p 8000:8000 -ti proyecto2 /bin/bash
```
Para iniciar el servidor, correr:
```
# Iniciar el servidor
python3 /home/proyecto2/manage.py runserver 0.0.0.0:8000
```

### Otros Comandos Útiles de Docker
```
docker image ls -a     # Mostrar todas las imagenes
docker ps -a           # Mostrar todos los contenedores
docker system prune -f # Limpiar imagenes y contenedores
```

### Otros Comandos Útiles
```
lsof -i -P -n # Revisar procesos en puertos
```

## Activando los Modelos para Crear la Base de Datos
```
python3 manage.py makemigrations app
python3 manage.py sqlmigrate app 0001
python3 manage.py migrate
```
