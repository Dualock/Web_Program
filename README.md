# Reserva de Espacios en Partidos
## IE724 Laboratory of programming and microcomputers, EIE, University of Costa Rica
## Rojas Emilio, Fonseca Dualock
## emilio.jrojas@ucr.ac.cr, dualok.fonseca@ucr.ac.cr

# Description
Creacion de un sitio Web para reservar espacios en un estadio de futbol.
Dicho sitio web cuenta con posibilidad de crear usuarios administradores o
"staff" los cuales pueden administrar la pagina facilmente desde el mismo sitio
y tambien usuarios normale, cuenta con un espacio para log in y para reservar asientos, tambien
tiene una seccion para acceder al perfil

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
python3 manage.py migrate                # inicializar base de datos.
python3 manage.py createsuperuser        # crear superusuario inicial.
python3 manage.py runserver 0.0.0.0:8000 # ejecutar servidor.
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
Por defecto se crea un superusuario con nombre de usuario admin y contraseña admin.
Para crear un nuevo superusuario:
```
python3 /home/proyecto2/manage.py createsuperuser # seguir las instrucciones
```
Con este nuevo superusuario se puede eliminar al superusuario por defecto.

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

### Compilacion y ejecucion automatica
Desde la carpeta Web_program
Ejecutar docker.sh para realizar la instalacion automatica de docker:
```
bash docker.sh
```
Desde la carpeta Web_program
Ejecutar config1.sh al para crear y correr la imagen de docker
```
bash config1.sh
```

Una vez dentro ejecutar el siguiente comando:
```
bash home/proyecto2/config2.sh
```

Una vez dentro de la imagen se ejecuta
```
bash /home/proyecto2/config2.sh
```
