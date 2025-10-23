from aiogram import Router
from aiogram.types import CallbackQuery
from app.core.keyboard_templates import KeyboardTemplates

router = Router()


@router.callback_query(lambda c: c.data == "roo_structure")
async def handle_roo_structure(callback: CallbackQuery):
    """Обработчик для РОО в структуре компании"""
    structure_text = """
РОО в структуре компании

Роль Руководителя Отдела Оценки - одна из самых важных в компании FRESH. Относится к продуктивному персоналу. Отдел оценки напрямую влияет на прибыль филиала, его развитие и репутацию компании.

Руководитель Отдела Оценки (РОО) напрямую подчиняется Управляющему филиалом, который отвечает за финансовые результаты и стратегию.

Руководитель Отдела Оценки (РОО) курирует экспертов отдела оценки и старшего эксперта по оценке.

В своей ежедневной работе взаимодействует с сопряженными отделами: КСО, ОП, HR, Сервис, АХО, Бухгалтерия, Отдел предпродажной подготовки.

Основные задачи Руководителя Отдела Оценки (РОО):
• Наполнение склада ликвидными автомобилями
• Эффективная работа отдела с клиентами  
• Оперативное решение кросс-функциональных задач
"""
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_cancel_keyboard()
    await callback.message.answer(structure_text, reply_markup=keyboard)
    await callback.answer()
