FROM python:3.12-slim 

WORKDIR /app

# Copiar el binario de uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Instalar dependencias utilizando uv (mucho más rápido que pip)
COPY requirements.txt . 
RUN uv pip install --system --no-cache -r requirements.txt

# Copiar el código fuente
COPY src ./src

EXPOSE 8000

# Usar --host 0.0.0.0 para exponer el puerto fuera del contenedor
CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0", "src/main.py"]