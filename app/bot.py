import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage

# Добавляем корневую папку в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings
from app.core.logging import setup_logging
from app.handlers import register_handlers


async def main():
    """Основная функция запуска бота"""
    # Настройка логирования
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Создание бота и диспетчера
    bot = Bot(token=settings.bot_token)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Регистрация обработчиков
    register_handlers(dp)
    
    logger.info("Бот запускается...")
    
    try:
        # Запуск бота
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()


# Точка входа для Docker
if __name__ == "__main__":
    asyncio.run(main())
