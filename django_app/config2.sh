#!/bin/bash
echo "Creando super usuario..."
python3 /Home/proyecto2/manage.py createsuperuser --username admin --email a@x

echo "Creando imagen"
sudo docker build . --file Dockerfile --tag proyecto2
echo "Iniciando contenedor a partir de la imagen creada..."
sudo docker run -p 8000:8000 -ti proyecto2 /bin/bash

echo "Activando modelos para bases de datos..."

echo "Corriendo el servidor..."
python3 /home/proyecto2/manage.py runserver 0.0.0.0:8000

