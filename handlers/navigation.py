from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_back_to_main(callback: CallbackQuery):
    """Обработчик возврата к главному меню"""
    current_text = callback.message.text
    print(f"DEBUG: back_to_main вызван! Текущий текст: {current_text[:100]}...")
    
    keyboard_templates = KeyboardTemplates()
    
    if "Выбери раздел который тебя интересует и FRESHBOT тебе поможет!" in current_text:
        # Уже на главном меню, ничего не делаем
        await callback.answer()
        return
    elif "Функционал РОО" in current_text and "Выберите направление работы:" in current_text:
        # Возвращаемся к главному меню
        main_text = "Выбери раздел который тебя интересует и FRESHBOT тебе поможет!"
        keyboard = await keyboard_templates.get_delayed_keyboard()
        await callback.message.edit_text(main_text, reply_markup=keyboard)
    elif "Работа с клиентом" in current_text and "Выберите направление контроля:" in current_text:
        # Возвращаемся к функционалу РОО
        from handlers.structure import handle_roo_functionality
        await handle_roo_functionality(callback)
    elif "Работа со складом" in current_text and "Выберите направление работы:" in current_text:
        # Возвращаемся к функционалу РОО
        from handlers.structure import handle_roo_functionality
        await handle_roo_functionality(callback)
    elif "Работа с персоналом" in current_text and "Выберите направление:" in current_text:
        # Возвращаемся к функционалу РОО
        from handlers.structure import handle_roo_functionality
        await handle_roo_functionality(callback)
    elif "Работа с цифрами" in current_text and "Выберите обязанность:" in current_text:
        # Возвращаемся к функционалу РОО
        from handlers.structure import handle_roo_functionality
        await handle_roo_functionality(callback)
    elif "Компетенции РОО" in current_text and "Выберите тип компетенций:" in current_text:
        # Возвращаемся к главному меню
        main_text = "Выбери раздел который тебя интересует и FRESHBOT тебе поможет!"
        keyboard = await keyboard_templates.get_delayed_keyboard()
        await callback.message.edit_text(main_text, reply_markup=keyboard)
    elif "Компетенции РОО" in current_text and ("Корпоративные" in current_text or "Технические" in current_text or "Управленческие" in current_text):
        # Возвращаемся к выбору типа компетенций
        from handlers.competencies import handle_competencies_back_to_types
        await handle_competencies_back_to_types(callback)
    elif "Подбор персонала" in current_text and "Выберите направление:" in current_text:
        # Возвращаемся к работе с персоналом
        from handlers.functionality.personnel import handle_functionality_personnel
        await handle_functionality_personnel(callback)
    elif "Контроль качества сделанной предпродажной подготовки" in current_text and "Выберите тип склада:" in current_text:
        # Возвращаемся к работе со складом
        from handlers.functionality.warehouse import handle_functionality_warehouse
        await handle_functionality_warehouse(callback)
    elif "Работа в роли закрывающего менеджера" in current_text and "Выберите цель:" in current_text:
        # Возвращаемся к работе с клиентом
        from handlers.functionality.client import handle_functionality_client
        await handle_functionality_client(callback)
    elif "Контроль отработки заявок от КЦ" in current_text and "Выберите направление:" in current_text:
        # Возвращаемся к работе с клиентом
        from handlers.functionality.client import handle_functionality_client
        await handle_functionality_client(callback)
    else:
        # По умолчанию возвращаемся к главному меню
        main_text = "Выбери раздел который тебя интересует и FRESHBOT тебе поможет!"
        keyboard = await keyboard_templates.get_delayed_keyboard()
        await callback.message.edit_text(main_text, reply_markup=keyboard)


async def handle_back_to_functionality(callback: CallbackQuery):
    """Обработчик возврата к функционалу РОО"""
    from handlers.structure import handle_roo_functionality
    await handle_roo_functionality(callback)


async def handle_back_to_client_menu(callback: CallbackQuery):
    """Обработчик возврата к меню работы с клиентом"""
    from handlers.functionality.client import handle_functionality_client
    await handle_functionality_client(callback)


async def handle_back_to_closing_manager(callback: CallbackQuery):
    """Обработчик возврата к меню закрывающего менеджера"""
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


async def handle_back_to_call_center(callback: CallbackQuery):
    """Обработчик возврата к меню контроля отработки заявок от КЦ"""
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


async def handle_back_to_warehouse_menu(callback: CallbackQuery):
    """Обработчик возврата к меню работы со складом"""
    from handlers.functionality.warehouse import handle_functionality_warehouse
    await handle_functionality_warehouse(callback)


async def handle_back_to_pre_sale(callback: CallbackQuery):
    """Обработчик возврата к меню контроля качества предпродажной подготовки"""
    from handlers.functionality.warehouse import handle_warehouse_pre_sale_quality
    await handle_warehouse_pre_sale_quality(callback)


async def handle_back_to_numbers_menu(callback: CallbackQuery):
    """Обработчик возврата к меню работы с цифрами"""
    from handlers.functionality.numbers import handle_functionality_numbers
    await handle_functionality_numbers(callback)


async def handle_back_to_personnel_menu(callback: CallbackQuery):
    """Обработчик возврата к меню работы с персоналом"""
    from handlers.functionality.personnel import handle_functionality_personnel
    await handle_functionality_personnel(callback)


async def handle_back_to_recruitment(callback: CallbackQuery):
    """Обработчик возврата к меню подбора персонала"""
    from handlers.functionality.personnel import handle_personnel_recruitment
    await handle_personnel_recruitment(callback)

