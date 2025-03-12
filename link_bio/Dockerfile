FROM python:3.13.2-slim

# Instalar dependencias
RUN apt-get update && apt-get install -y curl

# Variables de entorno
ENV REDIS_URL=redis://redis:6379 \
    API_URL=http://tu-dominio.com:8000

WORKDIR /app
COPY . .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar solo el backend
CMD ["reflex", "run", "--env", "prod", "--backend-only", "--loglevel", "info"]