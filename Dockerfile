FROM ubuntu:20.04

ENV TZ=America/Costa_Rica
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Información
LABEL version="1.0"
LABEL description="Custom docker image for proyecto2."

# Usuario root
USER root

# Instalar dependencias desde apt
RUN apt-get update \
    && apt-get --yes --no-install-recommends install \
       git wget screen lsof python3 python3-pip

# Instalar Django
RUN pip3 install Django

# Copiar proyecto
RUN mkdir -p /home/proyecto2
COPY django_app /home/proyecto2

# Habilitar el puerto 8000
EXPOSE 8000
