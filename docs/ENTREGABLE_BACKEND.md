#  Documentación de Proyecto: API Backend & Infraestructura

## 1. Información General
* **Nombre del Proyecto:** API Almacén de Ropa
* **Integrantes:**
  * Jesús Hernández
* **Repositorio (GitHub/GitLab):** [Agregar aquí el link público de GitHub]
* **Fecha de Entrega:** [DD/MM/AAAA]

---

## 2. Arquitectura y Stack Tecnológico

* **Lenguaje de Programación:** Python 3.13
* **Framework:** FastAPI
* **Gestor de Base de Datos:** SQLite
* **Ubicación de la DB:** Archivo local `app.db` dentro del proyecto / contenedor Docker local

### Diagrama de Flujo (Texto)
`[Cliente / Swagger / Postman] --(Petición HTTP)--> [Contenedor Docker con FastAPI] --(Consulta)--> [Base de datos SQLite app.db]`

---

## 3. Configuración de Infraestructura (Docker)

* **Imagen Base:** `python:3.13-slim`
* **Puerto Expuesto:** `8000`

### Variables de Entorno (.env)
* `DATABASE_URL`
* `SECRET_KEY`
* `ACCESS_TOKEN_EXPIRE_MINUTES`

---

## 4. Documentación de Endpoints

| Método | Ruta | Descripción | Cuerpo (JSON) / Params | Respuesta exitosa |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/health` | Verifica la salud de la API | N/A | `{"status":"ok","service":"api-almacen-ropa-jesus"}` |
| `POST` | `/auth/register` | Registra un usuario nuevo | `{"name":"Jesús","email":"jesus@mail.com","password":"123456","role":"staff"}` | `{"message":"Usuario registrado correctamente","user":{...}}` |
| `POST` | `/auth/login` | Autentica usuario y devuelve JWT | Form data: `username=jesus@mail.com`, `password=123456` | `{"access_token":"...","token_type":"bearer"}` |
| `GET` | `/users/` | Lista usuarios registrados | Requiere Bearer Token | `{"items":[...],"count":1}` |
| `POST` | `/packages/` | Registra un paquete | `{"tracking_number":"PKG-001","description":"Caja con playeras","status":"received"}` + Bearer Token | `{"message":"Package created","package":{...}}` |
| `POST` | `/attendance/` | Registra entrada o salida del usuario autenticado | `{"action":"check-in"}` + Bearer Token | `{"message":"Attendance registered","attendance":{...}}` |

---

## 5. Evidencias de Funcionamiento

### A. Contenedores en Ejecución
 Pegar aquí captura de `docker ps` o Docker Desktop mostrando el contenedor `api-almacen-ropa` ejecutándose.

### B. Conexión a Base de Datos
 Pegar aquí captura de la consola mostrando la API levantada correctamente y el archivo `app.db` generado.

### C. Prueba de Endpoint (Postman/Thunder Client/Swagger)
 Pegar aquí captura de una petición exitosa a `/auth/login`, `/users/` o `/packages/`.

---

## 6. Reflexión y Autoevaluación

###  Retos del Proyecto
* **Mayor dificultad técnica:** Integrar autenticación JWT, base de datos SQLite y estructura por capas dentro de una API REST funcional.
* **Solución aplicada:** Se reorganizó el proyecto para separar routers, modelos y dependencias, además de agregar configuración con Docker y variables de entorno.

###  Experiencia en la Clase de Backend
* **Análisis Personal:** Uno de los puntos más complejos ha sido configurar correctamente el entorno, levantar la API y conectar todos los componentes sin errores.
* **Causa del Bloqueo:** La mayor dificultad ha sido combinar instalación de herramientas, estructura del proyecto, manejo de dependencias y pruebas de endpoints.
* **Sugerencia de Mejora:** Ayudarían más ejemplos prácticos completos, especialmente desde cero, con instalación, ejecución, autenticación y pruebas paso a paso.

---

## 7. Estado Final del Proyecto
* **Estatus:** El proyecto funciona localmente con FastAPI, SQLite y autenticación JWT. También quedó preparada la configuración base para ejecutarse en Docker.
