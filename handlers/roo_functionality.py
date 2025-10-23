from aiogram import Router
from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates

router = Router()


@router.callback_query(lambda c: c.data == "roo_functionality")
async def handle_roo_functionality(callback: CallbackQuery):
    """Обработчик для функционала РОО"""
    functionality_text = "Функционал РОО"
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_cancel_keyboard()
    await callback.message.edit_text(functionality_text, reply_markup=keyboard)
    await callback.answer()


@router.callback_query(lambda c: c.data == "back_to_main")
async def handle_back_to_main(callback: CallbackQuery):
    """Обработчик кнопки Назад"""
    keyboard_templates = KeyboardTemplates()
    main_text = "Выберите раздел который тебя интересует и FRESHBOT тебе поможет!"
    keyboard = await keyboard_templates.get_delayed_keyboard()
    await callback.message.edit_text(main_text, reply_markup=keyboard)
    await callback.answer()
