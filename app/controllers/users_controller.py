from typing import Dict, List, Optional

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
        "active": active,
    }
    _USERS.append(new_user)
    _NEXT_ID += 1
    return new_user


def find_user(user_id: int) -> Optional[Dict]:
    for u in _USERS:
        if u.get("id") == user_id:
            return u
    return None


def update_user(user_id: int, name: str, role: str, active: bool) -> Optional[Dict]:
    u = find_user(user_id)
    if not u:
        return None

    u["name"] = name
    u["role"] = role
    u["active"] = active
    return u


def delete_user(user_id: int) -> bool:
    global _USERS
    before = len(_USERS)
    _USERS = [u for u in _USERS if u.get("id") != user_id]
    return len(_USERS) < before
