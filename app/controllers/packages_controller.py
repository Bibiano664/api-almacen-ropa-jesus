from datetime import datetime, timezone
from typing import Dict, List, Optional

_PACKAGES: List[Dict] = []
_NEXT_ID: int = 1


def list_packages() -> List[Dict]:
    return _PACKAGES


def create_package(description: str, origin: Optional[str] = None) -> Dict:
    """Create a package record (in-memory)."""
    global _NEXT_ID
    pkg = {
        "id": _NEXT_ID,
        "description": description,
        "origin": origin,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    _PACKAGES.append(pkg)
    _NEXT_ID += 1
    return pkg
