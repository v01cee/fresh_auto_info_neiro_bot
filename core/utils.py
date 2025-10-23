from typing import Any, Dict
import json


def format_user_data(user_data: Dict[str, Any]) -> str:
    """Форматирование данных пользователя для отображения"""
    if not user_data:
        return "Данные не найдены"
    
    formatted = []
    for key, value in user_data.items():
        if isinstance(value, (dict, list)):
            value = json.dumps(value, ensure_ascii=False, indent=2)
        formatted.append(f"{key}: {value}")
    
    return "\n".join(formatted)


def is_admin(user_id: int) -> bool:
    """Проверка, является ли пользователь администратором"""
    from core.config import settings
    return user_id in settings.admin_ids_list
