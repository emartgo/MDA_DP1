# Usar una imagen base de Python
FROM python:3.8

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

RUN pip install --upgrade pip

# Copiar el script y cualquier archivo de dependencia necesario
COPY ./db .
COPY requirements.txt .

# Instalar cualquier dependencia
RUN pip install -r requirements.txt
