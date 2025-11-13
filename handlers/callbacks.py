from aiogram.types import CallbackQuery
from handlers.structure import (
    handle_roo_structure,
    handle_roo_functionality,
    handle_roo_competencies,
    handle_rop_functionality,
    handle_search
)
from handlers.tasks import (
    handle_tasks_supplies,
    handle_tasks_client,
    handle_tasks_warehouse,
    handle_tasks_personnel,
    handle_tasks_numbers,
    handle_back_to_tasks
)
from handlers.warehouse import (
    handle_warehouse_pricing,
    handle_warehouse_discounts,
    handle_warehouse_control,
    handle_warehouse_classifieds,
    handle_warehouse_management,
    handle_back_to_warehouse,
    handle_warehouse_pricing_purchase,
    handle_warehouse_pricing_commission,
    handle_back_to_warehouse_pricing,
    handle_warehouse_control_readiness,
    handle_warehouse_control_placement,
    handle_back_to_warehouse_control,
    handle_warehouse_management_purchase,
    handle_warehouse_management_commission,
    handle_back_to_warehouse_management,
    handle_warehouse_management_purchase_10_10_10,
    handle_warehouse_management_purchase_reprep,
    handle_warehouse_management_purchase_45,
    handle_warehouse_management_purchase_reprice,
    handle_warehouse_management_purchase_auction,
    handle_back_to_warehouse_management_purchase,
    handle_warehouse_management_purchase_reprice_no_calls,
    handle_warehouse_management_purchase_reprice_has_calls,
    handle_warehouse_management_purchase_reprice_many_calls,
    handle_warehouse_management_purchase_reprice_few_calls,
    handle_back_to_warehouse_management_purchase_reprice,
    handle_back_to_warehouse_management_purchase_reprice_has_calls
)
from handlers.analytics import (
    handle_analytics_goals,
    handle_analytics_action,
    handle_analytics_indicators,
    handle_analytics_reports,
    handle_analytics_errors,
    handle_analytics_qlik,
    handle_back_to_analytics,
    handle_analytics_action_collect,
    handle_analytics_action_process,
    handle_analytics_action_interpret,
    handle_analytics_action_actions,
    handle_back_to_analytics_action
)
from handlers.functionality.client import (
    handle_functionality_client,
    handle_client_calls,
    handle_client_website,
    handle_client_crm_entry,
    handle_client_crm_consignor,
    handle_client_outgoing_calls,
    handle_client_documents,
    handle_client_payments,
    handle_client_closing_manager,
    handle_client_complaints,
    handle_client_call_center,
    handle_closing_conversion,
    handle_closing_conflicts,
    handle_call_center_interaction,
    handle_call_center_evaluation
)
from handlers.functionality.warehouse import (
    handle_functionality_warehouse,
    handle_warehouse_pricing_new_arrival,
    handle_warehouse_advertising,
    handle_warehouse_check_new_arrival,
    handle_warehouse_status_control,
    handle_warehouse_problematic,
    handle_warehouse_average_age,
    handle_warehouse_pre_sale_quality,
    handle_warehouse_buyout,
    handle_warehouse_consignment,
    handle_warehouse_45_plus
)
from handlers.functionality.personnel import (
    handle_functionality_personnel,
    handle_personnel_intern_adaptation,
    handle_personnel_burnout,
    handle_personnel_motivation,
    handle_personnel_training,
    handle_personnel_dismissal,
    handle_personnel_recruitment,
    handle_recruitment_vacancy,
    handle_recruitment_profile,
    handle_recruitment_interview
)
from handlers.functionality.numbers import (
    handle_functionality_numbers,
    handle_numbers_duty_2_1,
    handle_numbers_duty_2_2
)
from handlers.functionality.supplies import handle_functionality_supplies
from handlers.competencies import (
    handle_competencies_corporate,
    handle_competencies_technical,
    handle_competencies_management,
    handle_competencies_back_to_types
)
from handlers.navigation import (
    handle_back_to_main,
    handle_back_to_functionality,
    handle_back_to_client_menu,
    handle_back_to_closing_manager,
    handle_back_to_call_center,
    handle_back_to_warehouse_menu,
    handle_back_to_pre_sale,
    handle_back_to_numbers_menu,
    handle_back_to_personnel_menu,
    handle_back_to_recruitment
)


async def handle_search_with_state(callback: CallbackQuery, state):
    """Обёртка для handle_search с передачей state"""
    from handlers.search import handle_search_button
    await handle_search_button(callback, state)


async def handle_callback_queries(callback: CallbackQuery, state=None):
    """Главный роутер для всех callback запросов"""
    print(f"DEBUG: Обработчик callback вызван! Данные: {callback.data}")
    
    # Маппинг callback_data на обработчики
    callback_handlers = {
        # Структура РОО
        "roo_structure": handle_roo_structure,
        "roo_functionality": handle_roo_functionality,
        "roo_competencies": handle_roo_competencies,
        "rop_functionality": handle_rop_functionality,
        "search": lambda cb: handle_search_with_state(cb, state),
        
        # Задачи
        "tasks_supplies": handle_tasks_supplies,
        "tasks_client": handle_tasks_client,
        "tasks_warehouse": handle_tasks_warehouse,
        "tasks_personnel": handle_tasks_personnel,
        "tasks_numbers": handle_tasks_numbers,
        "back_to_tasks": handle_back_to_tasks,
        
        # Работа со складом
        "warehouse_pricing": handle_warehouse_pricing,
        "warehouse_discounts": handle_warehouse_discounts,
        "warehouse_control": handle_warehouse_control,
        "warehouse_classifieds": handle_warehouse_classifieds,
        "warehouse_management": handle_warehouse_management,
        "back_to_warehouse": handle_back_to_warehouse,
        
        # Ценообразование
        "warehouse_pricing_purchase": handle_warehouse_pricing_purchase,
        "warehouse_pricing_commission": handle_warehouse_pricing_commission,
        "back_to_warehouse_pricing": handle_back_to_warehouse_pricing,
        
        # Контроль состояния склада
        "warehouse_control_readiness": handle_warehouse_control_readiness,
        "warehouse_control_placement": handle_warehouse_control_placement,
        "back_to_warehouse_control": handle_back_to_warehouse_control,
        
        # Управление складом
        "warehouse_management_purchase": handle_warehouse_management_purchase,
        "warehouse_management_commission": handle_warehouse_management_commission,
        "back_to_warehouse_management": handle_back_to_warehouse_management,
        
        # Управление выкупным складом
        "warehouse_management_purchase_10_10_10": handle_warehouse_management_purchase_10_10_10,
        "warehouse_management_purchase_reprep": handle_warehouse_management_purchase_reprep,
        "warehouse_management_purchase_45": handle_warehouse_management_purchase_45,
        "warehouse_management_purchase_reprice": handle_warehouse_management_purchase_reprice,
        "warehouse_management_purchase_auction": handle_warehouse_management_purchase_auction,
        "back_to_warehouse_management_purchase": handle_back_to_warehouse_management_purchase,
        
        # Переоценка склада
        "warehouse_management_purchase_reprice_no_calls": handle_warehouse_management_purchase_reprice_no_calls,
        "warehouse_management_purchase_reprice_has_calls": handle_warehouse_management_purchase_reprice_has_calls,
        "warehouse_management_purchase_reprice_many_calls": handle_warehouse_management_purchase_reprice_many_calls,
        "warehouse_management_purchase_reprice_few_calls": handle_warehouse_management_purchase_reprice_few_calls,
        "back_to_warehouse_management_purchase_reprice": handle_back_to_warehouse_management_purchase_reprice,
        "back_to_warehouse_management_purchase_reprice_has_calls": handle_back_to_warehouse_management_purchase_reprice_has_calls,
        
        # Аналитика
        "analytics_goals": handle_analytics_goals,
        "analytics_action": handle_analytics_action,
        "analytics_indicators": handle_analytics_indicators,
        "analytics_reports": handle_analytics_reports,
        "analytics_errors": handle_analytics_errors,
        "analytics_qlik": handle_analytics_qlik,
        "back_to_analytics": handle_back_to_analytics,
        
        # Аналитика в действии
        "analytics_action_collect": handle_analytics_action_collect,
        "analytics_action_process": handle_analytics_action_process,
        "analytics_action_interpret": handle_analytics_action_interpret,
        "analytics_action_actions": handle_analytics_action_actions,
        "back_to_analytics_action": handle_back_to_analytics_action,
        
        # Функционал РОО
        "functionality_supplies": handle_functionality_supplies,
        "functionality_client": handle_functionality_client,
        "functionality_warehouse": handle_functionality_warehouse,
        "functionality_numbers": handle_functionality_numbers,
        "functionality_personnel": handle_functionality_personnel,
        
        # Работа с клиентом
        "client_calls": handle_client_calls,
        "client_website": handle_client_website,
        "client_crm_entry": handle_client_crm_entry,
        "client_crm_consignor": handle_client_crm_consignor,
        "client_outgoing_calls": handle_client_outgoing_calls,
        "client_documents": handle_client_documents,
        "client_payments": handle_client_payments,
        "client_closing_manager": handle_client_closing_manager,
        "client_complaints": handle_client_complaints,
        "client_call_center": handle_client_call_center,
        "closing_conversion": handle_closing_conversion,
        "closing_conflicts": handle_closing_conflicts,
        "call_center_interaction": handle_call_center_interaction,
        "call_center_evaluation": handle_call_center_evaluation,
        
        # Работа со складом
        "warehouse_pricing_new_arrival": handle_warehouse_pricing_new_arrival,
        "warehouse_advertising": handle_warehouse_advertising,
        "warehouse_check_new_arrival": handle_warehouse_check_new_arrival,
        "warehouse_status_control": handle_warehouse_status_control,
        "warehouse_problematic": handle_warehouse_problematic,
        "warehouse_average_age": handle_warehouse_average_age,
        "warehouse_pre_sale_quality": handle_warehouse_pre_sale_quality,
        "warehouse_buyout": handle_warehouse_buyout,
        "warehouse_consignment": handle_warehouse_consignment,
        "warehouse_45_plus": handle_warehouse_45_plus,
        
        # Работа с цифрами
        "numbers_duty_2_1": handle_numbers_duty_2_1,
        "numbers_duty_2_2": handle_numbers_duty_2_2,
        
        # Работа с персоналом
        "personnel_intern_adaptation": handle_personnel_intern_adaptation,
        "personnel_burnout": handle_personnel_burnout,
        "personnel_motivation": handle_personnel_motivation,
        "personnel_training": handle_personnel_training,
        "personnel_dismissal": handle_personnel_dismissal,
        "personnel_recruitment": handle_personnel_recruitment,
        "recruitment_vacancy": handle_recruitment_vacancy,
        "recruitment_profile": handle_recruitment_profile,
        "recruitment_interview": handle_recruitment_interview,
        
        # Компетенции
        "competencies_corporate": handle_competencies_corporate,
        "competencies_technical": handle_competencies_technical,
        "competencies_management": handle_competencies_management,
        "competencies_back_to_types": handle_competencies_back_to_types,
        
        # Навигация
        "back_to_main": handle_back_to_main,
        "back_to_functionality": handle_back_to_functionality,
        "back_to_client_menu": handle_back_to_client_menu,
        "back_to_closing_manager": handle_back_to_closing_manager,
        "back_to_call_center": handle_back_to_call_center,
        "back_to_warehouse_menu": handle_back_to_warehouse_menu,
        "back_to_pre_sale": handle_back_to_pre_sale,
        "back_to_numbers_menu": handle_back_to_numbers_menu,
        "back_to_personnel_menu": handle_back_to_personnel_menu,
        "back_to_recruitment": handle_back_to_recruitment,
    }
    
    # Вызываем соответствующий обработчик
    handler = callback_handlers.get(callback.data)
    if handler:
        await handler(callback)
    else:
        print(f"WARNING: Неизвестный callback_data: {callback.data}")
        await callback.answer()
        return
    
    await callback.answer()


def register_callback_handlers(dp):
    """Регистрация обработчика callback запросов"""
    # Регистрируем с поддержкой FSM state
    from aiogram.fsm.context import FSMContext
    
    async def callback_with_state(callback: CallbackQuery, state: FSMContext):
        await handle_callback_queries(callback, state)
    
    dp.callback_query.register(callback_with_state)

