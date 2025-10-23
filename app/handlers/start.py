import asyncio
from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from app.core.utils import is_admin
from app.core.keyboard_templates import KeyboardTemplates


async def start_command(message: Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
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
    
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_main_menu()
    
    await message.answer(welcome_text, reply_markup=keyboard)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Отправляем новое сообщение с инлайн-клавиатурой
    delayed_text = "Выберите раздел который тебя интересует и FRESHBOT тебе поможет!"
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
        case "team":
            team_text = """
👥 Работа с командой:

🔥 Лучший специалист - развивайте экспертизу
🎯 Играющий тренер - обучайте и мотивируйте
👨‍🏫 Наставник - передавайте опыт
🔍 Искатель кадров - находите таланты
🧠 Психолог и мотиватор - поддерживайте команду

Выберите действие:
"""
            keyboard = await keyboard_templates.get_team_menu()
            await callback.message.edit_text(team_text, reply_markup=keyboard)
            
        case "goals":
            goals_text = """
🎯 Управление целями:

📊 Постановка целей для команды
📈 Отслеживание прогресса
🎯 Анализ достижений
📋 Планирование задач

Выберите действие:
"""
            keyboard = await keyboard_templates.get_goals_menu()
            await callback.message.edit_text(goals_text, reply_markup=keyboard)
            
        case "processes":
            processes_text = """
📈 Управление процессами:

⚙️ Оптимизация рабочих процессов
📋 Документооборот
🔄 Автоматизация рутины
📊 Контроль качества

Выберите действие:
"""
            keyboard = await keyboard_templates.get_processes_menu()
            await callback.message.edit_text(processes_text, reply_markup=keyboard)
            
        case "motivation":
            motivation_text = """
🔥 Мотивация команды:

💪 Создание мотивирующей среды
🏆 Система поощрений
📈 Развитие карьеры
🤝 Командная работа

Выберите действие:
"""
            keyboard = await keyboard_templates.get_motivation_menu()
            await callback.message.edit_text(motivation_text, reply_markup=keyboard)
            
        case "analytics":
            analytics_text = """
📊 Аналитика и отчетность:

📈 KPI команды
📊 Эффективность процессов
📋 Отчеты по проектам
🎯 Анализ достижений

Выберите действие:
"""
            keyboard = await keyboard_templates.get_analytics_menu()
            await callback.message.edit_text(analytics_text, reply_markup=keyboard)
            
        case "settings":
            settings_text = """
⚙️ Настройки FRESHBOT:

🔔 Уведомления
🌐 Язык интерфейса
🔒 Приватность
📱 Персонализация

Выберите действие:
"""
            keyboard = await keyboard_templates.get_settings_menu()
            await callback.message.edit_text(settings_text, reply_markup=keyboard)
            
        case "back_to_main":
            keyboard = await keyboard_templates.get_main_menu()
            await callback.message.edit_text("🏠 Главное меню", reply_markup=keyboard)
            
        case "cancel":
            keyboard = await keyboard_templates.get_main_menu()
            await callback.message.edit_text("🏠 Главное меню", reply_markup=keyboard)
            
    
    await callback.answer()


def register_start_handlers(dp: Dispatcher):
    """Регистрация обработчиков стартовых команд"""
    dp.message.register(start_command, CommandStart())
    dp.message.register(help_command, Command("help"))
    dp.message.register(info_command, Command("info"))
    dp.callback_query.register(handle_callback_queries)
