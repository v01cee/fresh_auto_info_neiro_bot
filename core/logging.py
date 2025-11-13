import logging
import sys
from core.config import settings


def setup_logging():
    """Настройка логирования"""
    # Сначала настраиваем базовое логирование без зависимостей от settings
    level = logging.DEBUG
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True
    )
    
    logger = logging.getLogger(__name__)
    
    try:
        # Теперь можем использовать settings
        if hasattr(settings, 'debug'):
            level = logging.DEBUG if settings.debug else logging.INFO
            logging.getLogger().setLevel(level)
    except Exception as e:
        logger.warning(f"Не удалось загрузить настройки для логирования: {e}")
    
    # Настройка логирования для aiogram
    logging.getLogger('aiogram').setLevel(logging.INFO)
    logging.getLogger('aiogram.dispatcher').setLevel(logging.WARNING)
    logging.getLogger('aiogram.event').setLevel(logging.WARNING)
