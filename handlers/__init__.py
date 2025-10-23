from aiogram import Dispatcher
from handlers.start import register_start_handlers
from handlers.admin import register_admin_handlers
from handlers.roo_structure import router as roo_structure_router
from handlers.roo_functionality import router as roo_functionality_router
from handlers.roo_competencies import router as roo_competencies_router


def register_handlers(dp: Dispatcher):
    """Регистрация всех обработчиков"""
    register_start_handlers(dp)
    register_admin_handlers(dp)
    
    # Подключение роутеров
    dp.include_router(roo_structure_router)
    dp.include_router(roo_functionality_router)
    dp.include_router(roo_competencies_router)
