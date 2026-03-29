# Frontend (HTML/CSS/JS) – Almacén de Ropa

Este frontend es una página web sencilla (Frontend I) que **consume tu API FastAPI** usando `fetch()`.

## Requisitos
- Tener tu API corriendo con Uvicorn (por defecto `http://127.0.0.1:8000`).
- Si abres el HTML desde otra ruta/puerto, la API debe permitir **CORS**.

## Cómo correr

### 1) Levanta la API
En la carpeta del backend (raíz del proyecto):

```bash
uvicorn app.main:app --reload
```

Abre: `http://127.0.0.1:8000/docs` para verificar.

### 2) Corre el frontend
Opción A (recomendada): con la extensión **Live Server** en VS Code.
- Abre la carpeta `frontend/`
- Click derecho `index.html` → **Open with Live Server**

Opción B: con Python (servidor estático)

```bash
# Dentro de la carpeta frontend
python -m http.server 5500
```

Luego abre:
- `http://127.0.0.1:5500/`

## Configurar URL de tu API
Por defecto el frontend usa:

- `http://127.0.0.1:8000`

Si tu API corre en otra IP/puerto, en `app.js` cambia:

```js
const API_BASE = 'http://127.0.0.1:8000';
```

## Qué hace
- Muestra el **health** de la API.
- Lista y crea **Usuarios** (`/users/`)
- Lista y crea **Paquetes** (`/packages/`)
- Lista y crea **Asistencia** (`/attendance/`)

