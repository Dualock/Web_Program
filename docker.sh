#!/bin/bash
echo " Inicio de instalación de Docker "
echo " Tomado de https://www.hostinger.es/tutoriales/como-instalar-y-usar-docker-en-ubuntu "
echo "1. Actualizar el sistema."
sudo apt update;
sudo apt upgrade;
echo "2. Instalar paquetes de requisitos previos."
sudo apt-get install -y curl apt-transport-https ca-certificates software-properties-common;
echo "3. Agregar repositorios de Docker"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -;
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable";
sudo apt update;
echo "4. Instalar Docker."
sudo apt install -y docker-ce;
echo " Instalación Completa."
