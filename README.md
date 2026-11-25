# Proyecto Final - Sistemas Operativos (Arquitectura Multi-Cloud)

**Integrante:** Jacobo Castañeda Alarcón  
**Imagen Docker Hub:** `jako2230/so-backend:1.0`

## URLs en Producción (HTTPS)

- **Frontend (AWS EC2):** https://jacobo.scaleautomatization.tech/
- **Backend API (Azure VM):** https://api-jacobo.scaleautomatization.tech/api/sistemas

## Arquitectura Desplegada

1. **Frontend (AWS EC2 - Ubuntu):** Servido de forma estática mediante Nginx con certificado TLS gestionado por Let's Encrypt (Certbot). Interfaz diseñada con **Bento Grid**, **Soft UI (Neumorphism)** y efectos interactivos en Vanilla JS (`TechText`, tarjetas holográficas 3D, fondo `Flux` y `ScrollReveal`), con soporte para modo claro/oscuro, buscador instantáneo, ordenamiento cronológico, caché offline en `localStorage`, indicador de latencia (`ms`) y modales de inspección técnica y creación.
2. **Backend (Azure VM - Ubuntu):** API REST en Python (`Flask` + `Gunicorn` + `psycopg`) empaquetada en contenedor Docker (`jako2230/so-backend:1.0`) y expuesta únicamente hacia `127.0.0.1:8000` detrás de Nginx como proxy inverso con HTTPS y políticas CORS configuradas.
3. **Base de Datos (PostgreSQL 16):** Ejecutada en red privada interna de Docker Compose (sin puertos publicados hacia Internet) con persistencia mediante volumen nombrado (`pgdata`) e inicialización automática (`db/init.sql`), almacenando nombre, año, paradigma/tipo, descripción técnica, arquitectura de kernel y sistema de archivos.

## Endpoints de la API REST

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `GET` | `/api/salud` | Verifica la conectividad entre Flask y PostgreSQL (`{"estado": "ok"}`). |
| `GET` | `/api/sistemas` | Lista todos los sistemas operativos ordenados por año con sus especificaciones técnicas. |
| `POST` | `/api/sistemas` | Registra un nuevo sistema operativo en PostgreSQL (`nombre`, `anio`, `tipo`, `kernel`, `sistema_archivos`, `descripcion`). |
| `DELETE` | `/api/sistemas/<id>` | Elimina un registro de la base de datos por su identificador. |

## Estructura del Repositorio

```text
├── backend/
│   ├── app.py              # API REST en Flask con soporte CRUD y CORS
│   ├── Dockerfile          # Imagen basada en python:3.12-slim + Gunicorn
│   ├── requirements.txt    # Dependencias (Flask, psycopg, gunicorn)
│   └── .env.example        # Plantilla de variables de entorno
├── db/
│   └── init.sql            # Esquema de tabla sistemas_operativos y datos iniciales
├── frontend/
│   ├── index.html          # Estructura principal y modales de detalle/creación
│   ├── style.css           # Sistema de diseño Soft UI (modo claro/oscuro) y Bento Grid
│   ├── app.js              # Lógica de consumo REST, filtros, búsqueda, latencia y caché
│   ├── config.js           # URL pública del backend en Azure
│   ├── holo.js             # Efecto holográfico 3D interactivo en tarjetas
│   ├── flux.js             # Fondo animado en Canvas
│   ├── techtext.js         # Tipografía interactiva en cabecera
│   └── scrollreveal.js     # Animaciones de entrada al hacer scroll
├── nginx/                  # Configuraciones de servidor web (EC2) y proxy inverso (Azure)
└── compose.yaml            # Orquestación de servicios db y backend en Azure VM
```

## Despliegue Rápido

```bash
# 1. Construir y publicar imagen (PC local / GitHub Codespaces)
docker build --platform linux/amd64 -t jako2230/so-backend:1.0 ./backend
docker push jako2230/so-backend:1.0

# 2. Levantar servicios en Azure VM
cp backend/.env.example .env
docker compose up -d
```
