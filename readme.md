# API Almacén de Ropa

## Descripción (Dominio / Problema)
Esta API REST está diseñada para apoyar la operación diaria de un almacén de ropa. Permitirá registrar usuarios (empleados), controlar entradas y salidas (asistencia) y administrar el ingreso y almacenamiento de paquetes por día, con el fin de centralizar la información operativa y facilitar el seguimiento del trabajo diario.

El sistema está orientado a supervisores y personal administrativo del almacén, quienes necesitan consultar métricas básicas como paquetes ingresados por fecha y la ubicación de almacenamiento de cada paquete. Esta API será la base para futuras integraciones como dashboards, aplicaciones internas o módulos de inventario.


## Recursos principales (MVP)

Los recursos principales de la API son los siguientes:

- **users**: Representa a los usuarios o empleados del almacén.
- **attendance**: Registra la entrada y salida diaria de los usuarios.
- **packages**: Administra los paquetes que ingresan al almacén por día.
- **storage**: Controla la ubicación de almacenamiento de cada paquete.
- **teams**: Representa los equipos de trabajo dentro del almacén.


## Stack elegido y justificación

- **Framework:** FastAPI  
  Se eligió FastAPI porque permite construir APIs modernas con tipado, buen rendimiento y documentación automática (OpenAPI/Swagger), lo que facilita probar y documentar el proyecto como en un entorno real de industria.

- **Lenguaje/Runtime:** Python 3  
  Python permite desarrollo rápido y legible, con un ecosistema amplio para APIs y futuras integraciones.

- **Servidor ASGI:** Uvicorn  
  Uvicorn se utiliza para ejecutar la API de FastAPI localmente y en despliegue, ofreciendo buen desempeño.

- **Dependencias clave:**  
  - `fastapi`: framework principal de la API  
  - `uvicorn`: servidor para levantar la aplicación  

- **Base de datos tentativa:** PostgreSQL (por definir en siguientes fases)  
  Se sugiere PostgreSQL por ser estándar en industria y adecuada para manejar datos de operación e inventarios.

## Configuración de rutas y controladores

Esta sección documenta **cómo se organizó y configuró** la API para cumplir con la separación mínima de responsabilidades:

- **Rutas (routers):** definen endpoints y validan entrada/salida.
- **Controladores (controllers):** contienen la lógica (aunque sea simple), sin mezclarla con el enrutamiento.

### A) Estructura del proyecto

Carpetas principales:

- `app/main.py`  
  Punto de entrada. Crea la instancia de FastAPI e **incluye** los routers.

- `app/routers/`  
  Aquí vive el *routing* (endpoints). Cada archivo es un recurso:
  - `health.py`
  - `users.py`
  - `attendance.py`
  - `packages.py`

- `app/controllers/`  
  Aquí vive la lógica (controladores). Cada archivo responde al recurso:
  - `health_controller.py`
  - `users_controller.py`
  - `attendance_controller.py`
  - `packages_controller.py`

**¿Por qué separarlo?**  
Para que `main.py` y los routers se mantengan limpios, y la lógica se pueda cambiar o crecer después (por ejemplo, cuando agreguemos base de datos) sin reescribir rutas.

### B) Paso a paso técnico (mini tutorial)

1) **Crear la app principal**
   - Archivo: `app/main.py`
   - Se crea `app = FastAPI(...)`
   - Se registra un endpoint raíz `GET /` para confirmar que la API corre.

2) **Crear routers por recurso**
   - Archivos en `app/routers/*.py`
   - En cada router se crea:
     - `router = APIRouter(prefix="/recurso", tags=["recurso"])`
   - Se agregan endpoints con el método HTTP correcto (GET/POST).

3) **Crear controladores por recurso**
   - Archivos en `app/controllers/*.py`
   - Se crean funciones como `list_*()` y `create_*()` para que la lógica **no esté** en el router.
   - Para esta actividad (sin base de datos) usamos listas en memoria.

4) **Registrar routers en `main.py`**
   - En `app/main.py`:
     ```py
     from app.routers.users import router as users_router
     app.include_router(users_router)
     ```
   - Se repite para cada router.

### C) Endpoints implementados

#### 1) Health check
- **Método:** GET  
- **Ruta:** `/health`  
- **Qué hace:** confirma que la API está viva y entrega timestamp.

**Ejemplo de respuesta:**
```json
{
  "status": "ok",
  "service": "api-almacen-ropa-jesus",
  "timestamp": "2026-02-08T00:00:00+00:00"
}
```

#### 2) Users
- **Método:** GET  
- **Ruta:** `/users/`  
- **Qué hace:** lista usuarios (en memoria).

**Ejemplo de respuesta:**
```json
{
  "items": [],
  "count": 0
}
```

- **Método:** POST  
- **Ruta:** `/users/`  
- **Qué hace:** crea un usuario (en memoria).

**Body ejemplo:**
```json
{
  "name": "Jesús",
  "role": "Supervisor",
  "active": true
}
```

**Respuesta ejemplo (201):**
```json
{
  "message": "User created",
  "user": {
    "id": 1,
    "name": "Jesús",
    "role": "Supervisor",
    "active": true
  }
}
```

#### 3) Packages
- **Método:** GET  
- **Ruta:** `/packages/`  
- **Qué hace:** lista paquetes (en memoria).

- **Método:** POST  
- **Ruta:** `/packages/`  
- **Qué hace:** crea un paquete (en memoria).

**Body ejemplo:**
```json
{
  "description": "Caja con playeras",
  "origin": "Tijuana"
}
```

#### 4) Attendance
- **Método:** GET  
- **Ruta:** `/attendance/`  
- **Qué hace:** lista registros de asistencia (en memoria).

- **Método:** POST  
- **Ruta:** `/attendance/`  
- **Qué hace:** registra un check-in/check-out (en memoria).

**Body ejemplo:**
```json
{
  "user_id": 1,
  "action": "check-in"
}
```

### D) Cómo probar los endpoints

1) **Instalar dependencias**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

2) **Levantar el servidor**
Desde la raíz del proyecto:
```bash
uvicorn app.main:app --reload
```

3) **URL base**
- `http://127.0.0.1:8000`

4) **Probar en Swagger UI (recomendado)**
- `http://127.0.0.1:8000/docs`

5) **Ejemplos con curl**
```bash
curl http://127.0.0.1:8000/health

curl http://127.0.0.1:8000/users/

curl -X POST http://127.0.0.1:8000/users/ -H "Content-Type: application/json" -d "{"name":"Jesús","role":"Supervisor","active":true}"
```
