from aiogram import Dispatcher
from handlers.start import register_start_handlers
from handlers.admin import register_admin_handlers


def register_handlers(dp: Dispatcher):
    """Регистрация всех обработчиков"""
    register_start_handlers(dp)
    register_admin_handlers(dp)
