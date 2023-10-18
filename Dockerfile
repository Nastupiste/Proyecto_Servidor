# Utiliza una imagen base de Python 3
FROM python:3

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos (requirements.txt) a la imagen
COPY requirements.txt .

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual (tu aplicación) a la imagen en /app
COPY . .

# Especifica el comando a ejecutar cuando se inicie el contenedor
CMD [ "python", "main.py" ]
