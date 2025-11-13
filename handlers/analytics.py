from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_analytics_goals(callback: CallbackQuery):
    """Обработчик целей и задач аналитики"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_analytics_action(callback: CallbackQuery):
    """Обработчик аналитики в действии"""
    action_text = """Шаг 1. Сбор данных.

Автоматически — из CRM, вручную — от сотрудников.

Шаг 2. Обработка.

Используй простые инструменты (таблицы, дашборды). Главное — понять, что цифры "говорят".

Шаг 3. Интерпретация.

Задай вопросы:

Почему цифры такие?

Что изменилось в поведении клиентов или сотрудников?

Что нужно скорректировать?

Шаг 4. Действие.

На основе анализа — внедряй решения: обучение, перераспределение задач, корректировка процессов.
"""
    keyboard_templates = KeyboardTemplates()
    action_buttons = {
        "Сбор данных": "analytics_action_collect",
        "Обработка": "analytics_action_process",
        "Интерпретация": "analytics_action_interpret",
        "Действия": "analytics_action_actions",
        "<- Назад": "back_to_analytics"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(action_buttons, interval=1)
    await callback.message.edit_text(action_text, reply_markup=keyboard)
    await callback.answer()


async def handle_analytics_indicators(callback: CallbackQuery):
    """Обработчик основных показателей"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_analytics_reports(callback: CallbackQuery):
    """Обработчик форм отчетности"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_analytics_errors(callback: CallbackQuery):
    """Обработчик ошибок в аналитике"""
    errors_text = """❌ Отчёт ради отчёта (без выводов и действий).
❌ Много цифр, мало смысла.
❌ Игнорирование промежуточных данных.
❌ Сравнение сотрудников "в лоб" без контекста.
❌ Отсутствие регулярности.
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(errors_text, reply_markup=keyboard)
    await callback.answer()


async def handle_analytics_qlik(callback: CallbackQuery):
    """Обработчик Qlik"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_analytics_action_collect(callback: CallbackQuery):
    """Обработчик сбора данных"""
    import asyncio
    
    # Первое сообщение
    collect_text = """Где брать данные? Для формирования отчета основные данные берем из CRM. Так же мы можем брать данные из ежедневных отчетов менеджеров ОО, хостес, ОП, отдела маркетинга"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics_action"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(collect_text, reply_markup=keyboard)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Второе сообщение
    screens_text = "📂 Скрины из CRM где лежит отчет"
    await callback.message.answer(screens_text)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Убираем кнопку из первого сообщения
    await callback.message.edit_reply_markup(reply_markup=None)
    
    # Третье сообщение с кнопкой "Назад"
    marketing_text = "Отчет маркетолога показывает откуда к нам приходит трафик."
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics_action"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.answer(marketing_text, reply_markup=keyboard)
    
    await callback.answer()


async def handle_analytics_action_process(callback: CallbackQuery):
    """Обработчик обработки данных"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics_action"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_analytics_action_interpret(callback: CallbackQuery):
    """Обработчик интерпретации данных"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics_action"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_analytics_action_actions(callback: CallbackQuery):
    """Обработчик действий"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_analytics_action"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)
    await callback.answer()


async def handle_back_to_analytics_action(callback: CallbackQuery):
    """Обработчик возврата к аналитике в действии"""
    await handle_analytics_action(callback)


async def handle_back_to_analytics(callback: CallbackQuery):
    """Обработчик возврата к меню аналитики"""
    from handlers.tasks import handle_tasks_numbers
    await handle_tasks_numbers(callback)

