from core.keyboards import KeyboardOperations


class KeyboardTemplates:
    """Готовые шаблоны клавиатур для бота"""
    
    def __init__(self):
        self.keyboard_ops = KeyboardOperations()
    
    async def get_cancel_keyboard(self):
        """Клавиатура с кнопкой Назад"""
        buttons = {
            "<- Назад": "back_to_main"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=1)
    
    async def get_delayed_keyboard(self):
        """Клавиатура для отложенного сообщения"""
        buttons = {
            "Компетенции Руководителя отдела": "roo_competencies",
            "Структура продаж\\ взаимодействие отделов": "roo_structure",
            "Функционал РОП": "rop_functionality",
            "Функционал РОО": "roo_functionality",
            "Поиск": "search"
        }
        print(f"DEBUG: Создаем клавиатуру с кнопками: {buttons}")  # Отладочный лог
        return await self.keyboard_ops.create_keyboard(buttons, interval=1)
    
    async def get_tasks_keyboard(self):
        """Клавиатура с задачами для разбора"""
        buttons = {
            "Работа с поставками": "tasks_supplies",
            "Работа с клиентом": "tasks_client",
            "Работа со складом": "tasks_warehouse",
            "Работа с персоналом": "tasks_personnel",
            "Работа с цифрами": "tasks_numbers"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=1)
