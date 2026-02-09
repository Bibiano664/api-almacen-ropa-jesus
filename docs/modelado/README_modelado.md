# Modelado del Dominio y Datos — API Almacén de Ropa (Actividad 3)

## 1) Dominio (¿qué resuelve el sistema?)
Este proyecto modela la operación básica de un **almacén de ropa**. El sistema permite:
- Registrar **usuarios/empleados**.
- Registrar **paquetes** que ingresan al almacén (con tracking, descripción y estado).
- Asociar **detalles** de cada paquete (items/contenido).
- Registrar **asistencia** (check-in / check-out) de usuarios.
- Clasificar paquetes con **etiquetas (tags)** para facilitar búsqueda y organización.

El objetivo de esta actividad es definir un **modelo de datos** consistente (DER), un **modelo de dominio** (UML de clases) e implementar los **modelos ORM** en Python.

---

## 2) Entidades y decisiones clave
Se definieron mínimo 5 entidades, cumpliendo los requisitos:

### Entidades
- **User**: empleado/usuario del sistema.
- **Package** *(entidad principal del negocio)*: representa un paquete recibido/registrado.
- **PackageItem** *(entidad de detalle)*: representa cada item/contenido dentro de un paquete (1–N).
- **Attendance**: registro de entrada/salida del usuario (1–N desde User).
- **Tag**: catálogo de etiquetas para clasificar paquetes.
- **PackageTag** *(puente)*: resuelve relación **N–N** entre Package y Tag.
- **StorageLocation**: ubicación física sugerida (pasillo/estante).
- **PackageStorage** *(puente opcional)*: historial o asignación de paquete a ubicaciones (N–N).

> Nota: Aunque el requisito mínimo es 5, se incluyeron entidades extra para un modelo más realista.

### Reglas / constraints aplicadas (integridad)
- `users.email` **UNIQUE** (no puede repetirse).
- `packages.tracking_number` **UNIQUE**.
- `tags.name` **UNIQUE**.
- `package_tags (package_id, tag_id)` **UNIQUE** (evita duplicados).
- Campos obligatorios con `NOT NULL` (por ejemplo: `User.name`, `Package.tracking_number`, etc.).
- Timestamps en todas las entidades: `created_at`, `updated_at`.

---

## 3) Relaciones requeridas
### 1–N (uno a muchos)
- **User (1) → Attendance (N)**: un usuario puede tener muchos registros de asistencia.
- **User (1) → Package (N)**: un usuario puede registrar varios paquetes.
- **Package (1) → PackageItem (N)**: un paquete puede tener varios items.

### N–N (muchos a muchos)
- **Package (N) ↔ Tag (N)** mediante **PackageTag**.

---

## 4) Supuestos (assumptions)
- No se requiere autenticación en esta etapa.
- Los datos pueden persistirse en SQLite local durante desarrollo.
- `Attendance.type` se limita a valores como `in` / `out` (se modela como string, y puede evolucionar a Enum).
- `Package.status` se maneja como string (puede evolucionar a Enum: `received`, `stored`, `shipped`, etc.).
- `StorageLocation` es opcional para el MVP, pero se incluye como base de crecimiento.

---

## 5) Archivos de diagramas
En esta carpeta se incluyen:

- `DER.png` → Diagrama Entidad–Relación
- `UML_Clases.png` → Diagrama de Clases UML

---

## 6) Implementación ORM (Python)
Los modelos fueron implementados con **SQLAlchemy** en:
- `app/database.py` (engine, SessionLocal, Base)
- `app/models/*.py` (entidades del dominio)

### Conexión de BD
Se usa `DATABASE_URL` si existe en entorno, si no:
- `sqlite:///./app.db`

> Migraciones (Alembic) recomendadas para fases posteriores.
