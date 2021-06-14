#!/bin/bash
echo "Creando imagen"
sudo docker build . --file Dockerfile --tag proyecto2
echo "Iniciando contenedor a partir de la imagen creada..."
sudo docker run -p 8000:8000 -ti proyecto2 /bin/bash


