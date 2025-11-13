from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_tasks_supplies(callback: CallbackQuery):
    """Обработчик работы с поставками"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_tasks"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_tasks_client(callback: CallbackQuery):
    """Обработчик работы с клиентом"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_tasks"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_tasks_warehouse(callback: CallbackQuery):
    """Обработчик работы со складом"""
    warehouse_text = "Работа со складом:"
    keyboard_templates = KeyboardTemplates()
    warehouse_buttons = {
        "Ценообразование нового поступления": "warehouse_pricing",
        "Работа со скидками": "warehouse_discounts",
        "Контроль состояния склада": "warehouse_control",
        "Работа с класифайдами": "warehouse_classifieds",
        "Управление складом": "warehouse_management",
        "<- Назад": "back_to_tasks"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(warehouse_buttons, interval=1)
    await callback.message.edit_text(warehouse_text, reply_markup=keyboard)
    await callback.answer()


async def handle_tasks_personnel(callback: CallbackQuery):
    """Обработчик работы с персоналом"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_tasks"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_tasks_numbers(callback: CallbackQuery):
    """Обработчик работы с цифрами"""
    analytics_text = """🎯 1. Суть аналитики в FRESH Auto

Аналитика — это зеркало, в котором руководитель видит не настоящее, а будущее.
Её цель — не наказать, а понять, где растём, где теряем и как управлять лучше.

"Хороший руководитель не ждёт отчёта в конце месяца — он управляет цифрами каждый день."
"""
    keyboard_templates = KeyboardTemplates()
    analytics_buttons = {
        "Цели и задачи аналитики": "analytics_goals",
        "Аналитика в действии": "analytics_action",
        "Основные показатели": "analytics_indicators",
        "Формы отчетности": "analytics_reports",
        "Ошибки в Аналитике": "analytics_errors",
        "Qlik": "analytics_qlik",
        "<- Назад": "back_to_tasks"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(analytics_buttons, interval=1)
    await callback.message.edit_text(analytics_text, reply_markup=keyboard)
    await callback.answer()


async def handle_back_to_tasks(callback: CallbackQuery):
    """Обработчик возврата к меню задач"""
    from core.keyboard_templates import KeyboardTemplates
    keyboard_templates = KeyboardTemplates()
    tasks_keyboard = await keyboard_templates.get_tasks_keyboard()
    await callback.message.edit_text("Давайте подробнее разберем задачи", reply_markup=tasks_keyboard)
    await callback.answer()

