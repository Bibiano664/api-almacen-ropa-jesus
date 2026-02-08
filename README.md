# API Almacén de Ropa

## Descripción (Dominio / Problema)
Esta API REST está diseñada para apoyar la operación diaria de un almacén de ropa, centralizando información clave como empleados, asistencia y registro de paquetes que ingresan al almacén. El objetivo es reducir errores de captura, mejorar el seguimiento operativo y tener trazabilidad básica de lo que sucede cada día.

El sistema está dirigido a supervisores y personal administrativo que necesitan consultar rápidamente quién trabajó, qué entradas/salidas hubo y cuántos paquetes se registraron por fecha, para facilitar reportes y control interno. Esta API servirá como base para futuras integraciones (dashboard, app interna o módulo de inventario más completo).

---

## Recursos principales (MVP)

Los recursos principales de la API son los siguientes:

- **users**: Representa a los usuarios o empleados del almacén.
- **attendance**: Registra la entrada y salida diaria de los usuarios.
- **packages**: Administra los paquetes que ingresan al almacén por día.
- **storage**: Controla la ubicación de almacenamiento de cada paquete.
- **teams**: Representa los equipos de trabajo dentro del almacén.

---

## Stack elegido y justificación

### Framework principal
- **FastAPI**  
  Se eligió FastAPI porque permite construir APIs modernas con tipado, buen rendimiento y documentación automática (OpenAPI/Swagger), lo que facilita probar y documentar el proyecto como en un entorno real de industria.

### Lenguaje / Runtime
- **Python 3**  
  Python permite desarrollo rápido y legible, con un ecosistema amplio para APIs y futuras integraciones.

### Servidor ASGI
- **Uvicorn**  
  Uvicorn se utiliza para ejecutar la API de FastAPI localmente y en despliegue, ofreciendo buen desempeño.

### Dependencias clave
- `fastapi`: framework principal de la API  
- `uvicorn`: servidor ASGI para levantar la aplicación  

### Base de datos tentativa
- **PostgreSQL (por definir en siguientes fases)**  
  Se sugiere PostgreSQL por ser un estándar en la industria y adecuada para manejar datos de operación e inventarios.

---

## Estructura inicial del proyecto

```text
api-almacen-ropa-jesus/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  └─ routers/
│     ├─ __init__.py
│     ├─ users.py
│     ├─ attendance.py
│     └─ packages.py
├─ requirements.txt
├─ README.md
├─ .gitignore
└─ .env.example
