from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_functionality_supplies(callback: CallbackQuery):
    """Обработчик работы с поставками"""
    back_buttons = {"<- Назад": "back_to_functionality"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)

