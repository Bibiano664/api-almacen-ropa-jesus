from datetime import datetime, timezone


def get_health_status() -> dict:
    return {
        "status": "ok",
        "service": "api-almacen-ropa-jesus",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
