from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from core.keyboard_templates import KeyboardTemplates
from core.ai_service import ai_service
from core.config import settings
from handlers.structure import (
    handle_roo_structure,
    handle_roo_functionality,
    handle_roo_competencies,
    handle_rop_functionality
)
from handlers.tasks import (
    handle_tasks_numbers,
    handle_tasks_warehouse,
    handle_tasks_client,
    handle_tasks_personnel,
    handle_tasks_supplies
)
from handlers.analytics import (
    handle_analytics_goals,
    handle_analytics_action,
    handle_analytics_indicators,
    handle_analytics_reports,
    handle_analytics_errors,
    handle_analytics_qlik
)
from handlers.warehouse import (
    handle_warehouse_pricing,
    handle_warehouse_discounts,
    handle_warehouse_control,
    handle_warehouse_classifieds,
    handle_warehouse_management
)


class SearchStates(StatesGroup):
    waiting_for_query = State()


# Индекс контента для поиска - ВСЕ доступные разделы бота
CONTENT_INDEX = {
    # Основные разделы
    "roo_competencies": "Компетенции Руководителя отдела - корпоративные, технические и управленческие компетенции, навыки руководителя",
    "roo_structure": "Структура продаж и взаимодействие отделов - описание всех отделов компании (продажи, оценка, контакт-центр, F&I, ЕЦО, ППП, криминалистика, маркетинг, гостеприимство, юридическая служба, СВК, УК) и их взаимодействия",
    "rop_functionality": "Функционал РОП (Руководитель отдела продаж) - ежедневный график, сценарий дня РОП, распорядок дня руководителя отдела продаж, задачи РОП",
    "roo_functionality": "Функционал РОО (Руководитель отдела оценки) - ежедневный график, сценарий дня РОО, распорядок дня руководителя отдела оценки, задачи РОО",
    
    # Задачи
    "tasks_numbers": "Работа с цифрами, аналитика, анализ данных, отчетность, показатели, цифры, статистика, метрики, KPI, дашборды, Qlik",
    "tasks_warehouse": "Работа со складом, управление складом, ценообразование, скидки, контроль склада, классифайды, расстановка автомобилей, готовность склада, висяки, переоценка, аукцион, система 10/10/10",
    "tasks_client": "Работа с клиентом, клиенты, взаимодействие с клиентами, работа с заявками",
    "tasks_personnel": "Работа с персоналом, сотрудники, управление персоналом, обучение, мотивация",
    "tasks_supplies": "Работа с поставками, поставки, закупки",
    
    # Аналитика (подразделы)
    "analytics_goals": "Цели и задачи аналитики, цели аналитики, задачи аналитики",
    "analytics_action": "Аналитика в действии, как работает аналитика, применение аналитики, сбор данных, обработка, интерпретация, действия",
    "analytics_indicators": "Основные показатели, KPI, метрики, индикаторы эффективности",
    "analytics_reports": "Формы отчетности, отчеты, виды отчетов",
    "analytics_errors": "Ошибки в аналитике, типичные ошибки аналитики, проблемы с аналитикой",
    "analytics_qlik": "Qlik, система Qlik, работа с Qlik",
    
    # Работа со складом (подразделы)
    "warehouse_pricing": "Ценообразование нового поступления, установка цены, выкупной автомобиль, комиссионный автомобиль, цена автомобиля",
    "warehouse_discounts": "Работа со скидками, скидки клиентам, согласование скидки, персональная скидка",
    "warehouse_control": "Контроль состояния склада, готовность склада, расстановка автомобилей, стандарты расстановки",
    "warehouse_classifieds": "Работа с классифайдами, продвижение на классифайдах, Avito, Auto.ru, drom.ru, поднятие объявлений, реклама на классифайдах",
    "warehouse_management": "Управление складом, управление выкупным складом, управление комиссионным складом, контроль склада 45+, система 10/10/10, повторная предпродажка, переоценка, аукцион",
}


async def handle_search_button(callback: CallbackQuery, state: FSMContext = None):
    """Обработчик кнопки поиска"""
    search_text = """
🔍 Поиск

Введите ваш запрос, и я найду нужную информацию.

Например:
• "функционал роп"
• "компетенции руководителя"
• "структура отделов"
• "функции руководителя отдела оценки"
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_main"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(search_text, reply_markup=keyboard)
    
    # Устанавливаем состояние ожидания запроса, если state передан
    if state:
        try:
            await state.set_state(SearchStates.waiting_for_query)
        except:
            pass
    
    await callback.answer()


async def handle_search_query(message: Message, state: FSMContext):
    """Обработчик текстового запроса для поиска"""
    user_query = message.text.strip()
    
    if not user_query:
        await message.answer("Пожалуйста, введите ваш запрос.")
        return
    
    # Показываем, что идёт поиск
    search_message = await message.answer("🔍 Ищу информацию...")
    
    # Ищем контент через AI
    found_key = await ai_service.search_content(user_query, CONTENT_INDEX)
    
    if found_key:
        # Если нашли, вызываем соответствующий обработчик напрямую
        # Расширенный маппинг всех обработчиков
        handlers_map = {
            # Основные разделы
            "roo_structure": handle_roo_structure,
            "roo_functionality": handle_roo_functionality,
            "roo_competencies": handle_roo_competencies,
            "rop_functionality": handle_rop_functionality,
            
            # Задачи
            "tasks_numbers": handle_tasks_numbers,
            "tasks_warehouse": handle_tasks_warehouse,
            "tasks_client": handle_tasks_client,
            "tasks_personnel": handle_tasks_personnel,
            "tasks_supplies": handle_tasks_supplies,
            
            # Аналитика
            "analytics_goals": handle_analytics_goals,
            "analytics_action": handle_analytics_action,
            "analytics_indicators": handle_analytics_indicators,
            "analytics_reports": handle_analytics_reports,
            "analytics_errors": handle_analytics_errors,
            "analytics_qlik": handle_analytics_qlik,
            
            # Работа со складом
            "warehouse_pricing": handle_warehouse_pricing,
            "warehouse_discounts": handle_warehouse_discounts,
            "warehouse_control": handle_warehouse_control,
            "warehouse_classifieds": handle_warehouse_classifieds,
            "warehouse_management": handle_warehouse_management,
        }
        
        handler = handlers_map.get(found_key)
        if handler:
            # Удаляем сообщение "Ищу информацию..."
            await search_message.delete()
            
            # Создаём фиктивный callback с сообщением бота (которое можно редактировать)
            class FakeCallback:
                def __init__(self, bot_msg, user):
                    self.message = bot_msg
                    self.data = found_key
                    self.from_user = user
                
                async def answer(self):
                    pass
            
            # Создаём новое сообщение бота для обработчика
            # Отправляем пустое сообщение, которое потом будет отредактировано обработчиком
            bot = Bot(token=settings.bot_token)
            temp_message = await bot.send_message(
                chat_id=message.chat.id,
                text="Загрузка..."
            )
            
            fake_callback = FakeCallback(temp_message, message.from_user)
            # Вызываем обработчик
            await handler(fake_callback)
        else:
            not_found_text = f"❌ Раздел '{found_key}' найден, но обработчик не найден."
            keyboard_templates = KeyboardTemplates()
            back_buttons = {"<- Назад": "back_to_main"}
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
            await search_message.edit_text(not_found_text, reply_markup=keyboard)
    else:
        # Если не нашли
        not_found_text = f"""
❌ По вашему запросу "{user_query}" ничего не найдено.

Попробуйте использовать другие формулировки:
• "функционал роп" или "функционал РОП"
• "компетенции" или "компетенции руководителя"
• "структура" или "структура отделов"
• "функционал роо" или "функции роо"
"""
        keyboard_templates = KeyboardTemplates()
        back_buttons = {"<- Назад": "back_to_main"}
        keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
        await search_message.edit_text(not_found_text, reply_markup=keyboard)
    
    # Сбрасываем состояние
    await state.clear()


def register_search_handlers(dp: Dispatcher):
    """Регистрация обработчиков поиска"""
    # Регистрируем обработчик текстовых запросов в режиме поиска
    dp.message.register(
        handle_search_query,
        StateFilter(SearchStates.waiting_for_query)
    )

