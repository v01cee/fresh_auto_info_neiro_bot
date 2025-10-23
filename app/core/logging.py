import logging
import sys
from app.core.config import settings


def setup_logging():
    """Настройка логирования"""
    level = logging.DEBUG if settings.debug else logging.INFO
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )
    
    # Настройка логирования для aiogram
    logging.getLogger('aiogram').setLevel(logging.INFO)
    logging.getLogger('aiogram.dispatcher').setLevel(logging.WARNING)
