import asyncio
from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_functionality_client(callback: CallbackQuery):
    """Обработчик меню работы с клиентом"""
    client_text = """
Работа с клиентом

Выберите направление контроля:
"""
    client_buttons = {
        "Контроль качества отработки входящих звонков": "client_calls",
        "Контроль отработки заявок с сайта": "client_website", 
        "Контроль занесения клиента в CRM": "client_crm_entry",
        "Контроль ведения комитента в CRM": "client_crm_consignor",
        "Контроль качества исходящих звонков": "client_outgoing_calls",
        "Контроль корректно оформленных документов": "client_documents",
        "Контроль соблюдения сроков оплаты клиентам и партнерам": "client_payments",
        "Работа в роли закрывающего менеджера": "client_closing_manager",
        "Отработка рекламаций": "client_complaints",
        "Контроль отработки заявок от КЦ": "client_call_center",
        "<- Назад": "back_to_main"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(client_buttons, interval=1)
    await callback.message.edit_text(client_text, reply_markup=keyboard)


async def handle_client_calls(callback: CallbackQuery):
    """Обработчик контроля качества входящих звонков"""
    back_buttons = {"<- Назад": "back_to_client_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_client_website(callback: CallbackQuery):
    """Обработчик контроля отработки заявок с сайта"""
    back_buttons = {"<- Назад": "back_to_client_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_client_crm_entry(callback: CallbackQuery):
    """Обработчик контроля занесения клиента в CRM"""
    back_buttons = {"<- Назад": "back_to_client_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_client_crm_consignor(callback: CallbackQuery):
    """Обработчик контроля ведения комитента в CRM"""
    back_buttons = {"<- Назад": "back_to_client_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_client_outgoing_calls(callback: CallbackQuery):
    """Обработчик контроля качества исходящих звонков"""
    back_buttons = {"<- Назад": "back_to_client_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_client_documents(callback: CallbackQuery):
    """Обработчик контроля корректно оформленных документов"""
    back_buttons = {"<- Назад": "back_to_client_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_client_payments(callback: CallbackQuery):
    """Обработчик контроля соблюдения сроков оплаты"""
    back_buttons = {"<- Назад": "back_to_client_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_client_closing_manager(callback: CallbackQuery):
    """Обработчик работы в роли закрывающего менеджера"""
    closing_manager_text = """
Работа в роли закрывающего менеджера

Выберите цель:
"""
    closing_manager_buttons = {
        "Цель: повышение конверсии": "closing_conversion",
        "Цель: предотвращение конфликтных ситуаций": "closing_conflicts",
        "<- Назад": "back_to_client_menu"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(closing_manager_buttons, interval=1)
    await callback.message.edit_text(closing_manager_text, reply_markup=keyboard)


async def handle_client_complaints(callback: CallbackQuery):
    """Обработчик отработки рекламаций"""
    back_buttons = {"<- Назад": "back_to_client_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_client_call_center(callback: CallbackQuery):
    """Обработчик контроля отработки заявок от КЦ"""
    call_center_text = """
Контроль отработки заявок от КЦ

Выберите направление:
"""
    call_center_buttons = {
        "Взаимодействие с КЦ": "call_center_interaction",
        "Контроль ЭО": "call_center_evaluation",
        "<- Назад": "back_to_client_menu"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(call_center_buttons, interval=1)
    await callback.message.edit_text(call_center_text, reply_markup=keyboard)


async def handle_closing_conversion(callback: CallbackQuery):
    """Обработчик цели: повышение конверсии"""
    back_buttons = {"<- Назад": "back_to_closing_manager"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_closing_conflicts(callback: CallbackQuery):
    """Обработчик цели: предотвращение конфликтных ситуаций"""
    back_buttons = {"<- Назад": "back_to_closing_manager"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_call_center_interaction(callback: CallbackQuery):
    """Обработчик взаимодействия с КЦ"""
    back_buttons = {"<- Назад": "back_to_call_center"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_call_center_evaluation(callback: CallbackQuery):
    """Обработчик контроля ЭО"""
    back_buttons = {"<- Назад": "back_to_call_center"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)

