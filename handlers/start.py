import asyncio
from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def start_command(message: Message):
    """Обработчик команды /start"""
    username = message.from_user.username or "Пользователь"
    
    welcome_text = f"""
👋 Добро пожаловать, {username}!

Я FRESHBOT - ваш помощник в повседневной работе с командой, целями и процессами!

🔥 Как руководитель отдела оценки компании FRESH, вы:
• Лучший специалист
• Эксперт по продукту  
• Играющий тренер
• Наставник
• Искатель кадров
• Психолог и мотиватор

Но даже сильному лидеру и профессионалу порой нужна поддержка!
Поэтому я здесь, чтобы помочь вам! 😊

Выберите действие из меню ниже:
"""
    
    await message.answer(welcome_text)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Отправляем новое сообщение с инлайн-клавиатурой
    delayed_text = "Выберите раздел который тебя интересует и FRESHBOT тебе поможет!"
    keyboard_templates = KeyboardTemplates()
    delayed_keyboard = await keyboard_templates.get_delayed_keyboard()
    await message.answer(delayed_text, reply_markup=delayed_keyboard)


async def help_command(message: Message):
    """Обработчик команды /help"""
    help_text = """
📖 Помощь по боту:

/start - Начать работу с ботом
/help - Показать это сообщение
/info - Информация о боте

Для получения помощи обратитесь к администратору.
"""
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_cancel_keyboard()
    await message.answer(help_text, reply_markup=keyboard)


async def info_command(message: Message):
    """Обработчик команды /info"""
    info_text = """
ℹ️ Информация о боте:

🤖 Название: Fresh Auto Info Neiro Bot
📝 Описание: Бот для автоматической обработки информации с использованием нейросетей
🔧 Версия: 1.0.0
👨‍💻 Разработчик: v01cee
"""
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_cancel_keyboard()
    await message.answer(info_text, reply_markup=keyboard)


async def handle_callback_queries(callback: CallbackQuery):
    """Обработчик callback запросов от inline клавиатур"""
    keyboard_templates = KeyboardTemplates()
    
    match callback.data:
        case "back_to_main":
            main_text = "Выберите раздел который тебя интересует и FRESHBOT тебе поможет!"
            keyboard = await keyboard_templates.get_delayed_keyboard()
            await callback.message.edit_text(main_text, reply_markup=keyboard)
    
    await callback.answer()


def register_start_handlers(dp: Dispatcher):
    """Регистрация обработчиков стартовых команд"""
    dp.message.register(start_command, CommandStart())
    dp.message.register(help_command, Command("help"))
    dp.message.register(info_command, Command("info"))
    dp.callback_query.register(handle_callback_queries)
