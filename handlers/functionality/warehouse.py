from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_functionality_warehouse(callback: CallbackQuery):
    """Обработчик меню работы со складом"""
    warehouse_text = """
Работа со складом

Выберите направление работы:
"""
    warehouse_buttons = {
        "Ценообразование нового поступления": "warehouse_pricing_new_arrival",
        "Вывод в рекламу": "warehouse_advertising",
        "Проверка свежего поступления": "warehouse_check_new_arrival",
        "Контроль состояния склада": "warehouse_status_control",
        "Работа с проблемным складом": "warehouse_problematic",
        "Средний возраст склада": "warehouse_average_age",
        "Контроль качества сделанной предпродажной подготовки": "warehouse_pre_sale_quality",
        "<- Назад": "back_to_functionality"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(warehouse_buttons, interval=1)
    await callback.message.edit_text(warehouse_text, reply_markup=keyboard)


async def handle_warehouse_pricing_new_arrival(callback: CallbackQuery):
    """Обработчик ценообразования нового поступления"""
    back_buttons = {"<- Назад": "back_to_warehouse_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_warehouse_advertising(callback: CallbackQuery):
    """Обработчик вывода в рекламу"""
    back_buttons = {"<- Назад": "back_to_warehouse_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_warehouse_check_new_arrival(callback: CallbackQuery):
    """Обработчик проверки свежего поступления"""
    back_buttons = {"<- Назад": "back_to_warehouse_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_warehouse_status_control(callback: CallbackQuery):
    """Обработчик контроля состояния склада"""
    back_buttons = {"<- Назад": "back_to_warehouse_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_warehouse_problematic(callback: CallbackQuery):
    """Обработчик работы с проблемным складом"""
    back_buttons = {"<- Назад": "back_to_warehouse_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_warehouse_average_age(callback: CallbackQuery):
    """Обработчик среднего возраста склада"""
    back_buttons = {"<- Назад": "back_to_warehouse_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_warehouse_pre_sale_quality(callback: CallbackQuery):
    """Обработчик контроля качества предпродажной подготовки"""
    pre_sale_text = """
Контроль качества сделанной предпродажной подготовки

Выберите тип склада:
"""
    pre_sale_buttons = {
        "Выкупной склад": "warehouse_buyout",
        "Комиссионный склад": "warehouse_consignment",
        "Склад 45+": "warehouse_45_plus",
        "<- Назад": "back_to_warehouse_menu"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(pre_sale_buttons, interval=1)
    await callback.message.edit_text(pre_sale_text, reply_markup=keyboard)


async def handle_warehouse_buyout(callback: CallbackQuery):
    """Обработчик выкупного склада"""
    back_buttons = {"<- Назад": "back_to_pre_sale"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_warehouse_consignment(callback: CallbackQuery):
    """Обработчик комиссионного склада"""
    back_buttons = {"<- Назад": "back_to_pre_sale"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_warehouse_45_plus(callback: CallbackQuery):
    """Обработчик склада 45+"""
    back_buttons = {"<- Назад": "back_to_pre_sale"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)

