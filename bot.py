import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage

# Добавляем корневую папку в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config import settings
from core.logging import setup_logging
from handlers import register_handlers


async def main():
    """Основная функция запуска бота"""
    # Настройка логирования
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Инициализация бота...")
        
        # Проверка токена
        if not settings.bot_token:
            logger.error("Токен бота не найден! Проверьте файл .env")
            return
        
        logger.info(f"Токен бота загружен (длина: {len(settings.bot_token)} символов)")
        
        # Создание бота и диспетчера
        logger.info("Создание экземпляра бота...")
        bot = Bot(token=settings.bot_token)
        
        logger.info("Создание хранилища состояний...")
        storage = MemoryStorage()
        
        logger.info("Создание диспетчера...")
        dp = Dispatcher(storage=storage)
        
        # Регистрация обработчиков
        logger.info("Регистрация обработчиков...")
        register_handlers(dp)
        logger.info("Обработчики зарегистрированы")
        
        # Проверка подключения
        logger.info("Проверка подключения к Telegram API...")
        bot_info = await bot.get_me()
        logger.info(f"Бот успешно подключен: @{bot_info.username} ({bot_info.first_name})")
        
        logger.info("Запуск polling...")
        # Запуск бота
        await dp.start_polling(bot, skip_updates=True)
        
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}", exc_info=True)
        import traceback
        traceback.print_exc()
    finally:
        if 'bot' in locals():
            logger.info("Закрытие сессии бота...")
            try:
                await bot.session.close()
            except:
                pass
            logger.info("Бот остановлен")


# Точка входа для Docker
if __name__ == "__main__":
    asyncio.run(main())
