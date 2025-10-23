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
    await callback.message.answer(functionality_text, reply_markup=keyboard)
    await callback.answer()
