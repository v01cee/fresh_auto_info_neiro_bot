from aiogram import Dispatcher
from handlers.commands import register_commands_handlers
from handlers.callbacks import register_callback_handlers
from handlers.admin import register_admin_handlers
from handlers.search import register_search_handlers
from handlers.photo import register_photo_handlers


def register_handlers(dp: Dispatcher):
    """Регистрация всех обработчиков"""
    register_commands_handlers(dp)
    register_callback_handlers(dp)
    register_search_handlers(dp)
    register_photo_handlers(dp)
    register_admin_handlers(dp)
