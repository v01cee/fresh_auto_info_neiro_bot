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
            "РОО в структуре компании": "roo_structure",
            "Функционал РОО": "roo_functionality", 
            "Компетенции РОО": "roo_competencies"
        }
        print(f"DEBUG: Создаем клавиатуру с кнопками: {buttons}")  # Отладочный лог
        return await self.keyboard_ops.create_keyboard(buttons, interval=1)
