from typing import Dict, List

_USERS: List[Dict] = []
_NEXT_ID: int = 1


def list_users() -> List[Dict]:
    return _USERS


def create_user(name: str, role: str, active: bool) -> Dict:
    global _NEXT_ID

    new_user = {
        "id": _NEXT_ID,
        "name": name,
        "role": role,
        "active": active
    }
    _USERS.append(new_user)
    _NEXT_ID += 1
    return new_user
