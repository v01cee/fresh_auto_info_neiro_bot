from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from app.core.utils import is_admin
from app.core.keyboard_templates import KeyboardTemplates


async def admin_command(message: Message):
    """Обработчик команды /admin"""
    user_id = message.from_user.id
    
    if not is_admin(user_id):
        await message.answer("❌ У вас нет прав администратора!")
        return
    
    admin_text = """
👑 Панель администратора:

Выберите действие из меню ниже:
"""
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_admin_menu()
    await message.answer(admin_text, reply_markup=keyboard)


async def stats_command(message: Message):
    """Обработчик команды /stats"""
    user_id = message.from_user.id
    
    if not is_admin(user_id):
        await message.answer("❌ У вас нет прав администратора!")
        return
    
    # Здесь будет логика получения статистики
    stats_text = """
📊 Статистика бота:

👥 Всего пользователей: 0
📝 Сообщений сегодня: 0
🔄 Активных сессий: 0
"""
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_cancel_keyboard()
    await message.answer(stats_text, reply_markup=keyboard)


async def broadcast_command(message: Message):
    """Обработчик команды /broadcast"""
    user_id = message.from_user.id
    
    if not is_admin(user_id):
        await message.answer("❌ У вас нет прав администратора!")
        return
    
    await message.answer("📢 Функция рассылки будет добавлена в следующих версиях!")


async def handle_admin_callbacks(callback: CallbackQuery):
    """Обработчик админских callback запросов"""
    user_id = callback.from_user.id
    
    if not is_admin(user_id):
        await callback.answer("❌ У вас нет прав администратора!", show_alert=True)
        return
    
    keyboard_templates = KeyboardTemplates()
    
    match callback.data:
        case "admin_users":
            users_text = """
👥 Управление пользователями:

📊 Всего пользователей: 0
🟢 Активных: 0
🔴 Заблокированных: 0
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(users_text, reply_markup=keyboard)
            
        case "admin_stats":
            stats_text = """
📊 Статистика бота:

👥 Всего пользователей: 0
📝 Сообщений сегодня: 0
🔄 Активных сессий: 0
📈 Конверсия: 0%
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(stats_text, reply_markup=keyboard)
            
        case "admin_broadcast":
            broadcast_text = """
📢 Рассылка сообщений:

Функция рассылки будет добавлена в следующих версиях!
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(broadcast_text, reply_markup=keyboard)
            
        case "admin_settings":
            settings_text = """
⚙️ Настройки бота:

🔧 Основные настройки
🔔 Уведомления
🛡️ Безопасность
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(settings_text, reply_markup=keyboard)
    
    await callback.answer()


def register_admin_handlers(dp: Dispatcher):
    """Регистрация обработчиков админских команд"""
    dp.message.register(admin_command, Command("admin"))
    dp.message.register(stats_command, Command("stats"))
    dp.message.register(broadcast_command, Command("broadcast"))
    dp.callback_query.register(handle_admin_callbacks)
