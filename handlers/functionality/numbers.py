from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_functionality_numbers(callback: CallbackQuery):
    """Обработчик меню работы с цифрами"""
    numbers_text = """
Работа с цифрами

Выберите обязанность:
"""
    numbers_buttons = {
        "Обязанность 2.1": "numbers_duty_2_1",
        "Обязанность 2.2": "numbers_duty_2_2",
        "<- Назад": "back_to_functionality"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(numbers_buttons, interval=1)
    await callback.message.edit_text(numbers_text, reply_markup=keyboard)


async def handle_numbers_duty_2_1(callback: CallbackQuery):
    """Обработчик обязанности 2.1"""
    back_buttons = {"<- Назад": "back_to_numbers_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_numbers_duty_2_2(callback: CallbackQuery):
    """Обработчик обязанности 2.2"""
    back_buttons = {"<- Назад": "back_to_numbers_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)

