# Revisión del proyecto: API Almacén de Ropa

## Lo que ya cumple tu proyecto

- API construida con **FastAPI**.
- Base de datos local **SQLite** (`app.db`).
- Modelos ORM con **SQLAlchemy**.
- Registro y login con **JWT** en `/auth/register` y `/auth/login`.
- Endpoint protegido `/auth/me`.
- Diagramas incluidos en `docs/modelado/`.
- Archivo `README.md` y `.env.example`.

## Lo que le faltaba o estaba débil

1. **Faltaban dependencias** en `requirements.txt`.
   - No estaban `python-jose`, `passlib`, `python-multipart` ni `email-validator`.

2. **No había archivos de Docker**.
   - Faltaban `Dockerfile` y `docker-compose.yml`.

3. **Los endpoints de users/packages/attendance trabajaban en memoria**.
   - Eso chocaba con el hecho de que el proyecto ya tenía SQLite y modelos reales.

4. **`.env.example` estaba vacío**.
   - Ya no servía como guía de instalación.

5. **La clave JWT estaba fija en el código**.
   - Se movió para que pueda configurarse por variable de entorno.

6. **Faltaba un documento del entregable** alineado al formato del profe.
   - Se agregó `docs/ENTREGABLE_BACKEND.md`.

## Cambios realizados

- Se completó `requirements.txt`.
- Se llenó `.env.example`.
- Se actualizó `app/security.py` para usar variables de entorno.
- Se reescribieron los routers:
  - `app/routers/users.py`
  - `app/routers/packages.py`
  - `app/routers/attendance.py`
- Se agregaron:
  - `Dockerfile`
  - `docker-compose.yml`
  - `docs/ENTREGABLE_BACKEND.md`

## Recomendaciones antes de entregar

- **No subas `.venv/` al repositorio**.
- **No subas `.git/` dentro del ZIP del proyecto**.
- **No subas `__pycache__/`**.
- Puedes decidir si quieres subir `app.db`; para entrega escolar normalmente sí ayuda porque demuestra estructura y tablas, pero en proyectos reales suele ignorarse.
- Toma capturas de:
  - `docker ps`
  - `docker image ls`
  - Swagger o Postman
  - navegador en `http://127.0.0.1:8000/docs`

## Cómo correr el proyecto

### Local
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker
```bash
docker compose up --build
```

## Endpoints principales sugeridos para mostrar al profe

- `GET /health`
- `POST /auth/register`
- `POST /auth/login`
- `GET /users/` (con Bearer Token)
- `POST /packages/` (con Bearer Token)
- `POST /attendance/` (con Bearer Token)
