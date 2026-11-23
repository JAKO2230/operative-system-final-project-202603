# Proyecto Final - Sistemas Operativos (Arquitectura Multi-Cloud)

**Integrante:** Jacobo Castañeda  
**Imagen Docker Hub:** `jako2230/so-backend:1.0`

## URLs en Producción (HTTPS)
* **Frontend (AWS EC2):** https://scaleautomatization.tech
* **Backend API (Azure VM):** https://scaleautomatization.tech

## Arquitectura Desplegada
1. **Frontend (AWS EC2 - Ubuntu):** Servido de forma estática mediante Nginx con certificado TLS gestionado por Let's Encrypt (Certbot). Interfaz diseñada con Bento Grid y Soft UI (Neumorphism) con soporte para modo claro/oscuro.
2. **Backend (Azure VM - Ubuntu):** API REST en Python (Flask + Gunicorn) empaquetada en contenedor Docker (`jako2230/so-backend:1.0`) y expuesta únicamente hacia `127.0.0.1:8000` detrás de Nginx como proxy inverso con HTTPS.
3. **Base de Datos (PostgreSQL 16):** Ejecutada en red privada interna de Docker Compose con persistencia mediante volumen nombrado (`pgdata`) e inicialización automática (`db/init.sql`).

## Despliegue Rápido
```bash
# Construir y publicar imagen (PC local / Codespaces)
docker build -t jako2230/so-backend:1.0 ./backend
docker push jako2230/so-backend:1.0

# Levantar servicios en Azure VM
cp backend/.env.example .env
docker compose up -d
```
