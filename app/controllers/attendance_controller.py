from datetime import datetime, timezone
from typing import Dict, List

_ATTENDANCE: List[Dict] = []
_NEXT_ID: int = 1


def list_attendance() -> List[Dict]:
    return _ATTENDANCE


def create_attendance(user_id: int, action: str) -> Dict:
    """Create an attendance record (in-memory)."""
    global _NEXT_ID
    record = {
        "id": _NEXT_ID,
        "user_id": user_id,
        "action": action,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    _ATTENDANCE.append(record)
    _NEXT_ID += 1
    return record
