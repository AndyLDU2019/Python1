# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos (si es necesario) y el código fuente
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente al contenedor
COPY . /app/

# Exponer el puerto donde Flask escucha
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
