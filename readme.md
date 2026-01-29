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