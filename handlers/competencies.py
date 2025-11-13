from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_competencies_corporate(callback: CallbackQuery):
    """Обработчик корпоративных компетенций"""
    corporate_text = """
Уважение к сотрудникам и клиентам - это твоя способность понимать и удовлетворять потребности клиента

Нацеленность на результат -способность достигать цели, демонстрировать высокий уровень качества исполнения работы

Постоянное обучение и развитие это готовность совершенствовать себя и свою работу

Командность - способность успешно работать с другими сотрудниками компании, добиваться скоординированных действий для реализации целей компании

Ответственность - способность адекватно отвечать за то, что ему поручено либо за то, что он взял на себя сам

Способность к трансформациям -готовность быстро, открыто и гибко менять свой жизненный и профессиональный уклад в ответ на изменения среды
"""
    back_buttons = {"<- Назад": "competencies_back_to_types"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(corporate_text, reply_markup=keyboard)


async def handle_competencies_technical(callback: CallbackQuery):
    """Обработчик технических компетенций"""
    technical_text = """
Работа с ценообразованием:
- Знание категорийности качества и ликвидности ТС
- Знание элементов финального ценообразование (вложения, состояние, рынок, прогнозируемая рентабельность, количество ДТП, история)
- Умение управлять комиссионным складом
- Умение управлять "Стоком 45+" - вовремя работать с ценообразованием склада
- Навык контроля качества звонка, регулярности взаимодействия с комитентом, состояния а/м комиссионного стока

Работа с показателями и отчетностью
- Умение анализировать показатели эффективности ОО. выявлять зоны внимания
- Умение прогнозировать и планировать операционные показатели ОО на будущие периоды
- Умение формировать отечность ОО, вести табель учета рабочего времени.

Работа со смежными подразделениями
- Умение анализировать ключевые показатели эффективности смежных подразделений
- Знание кросс функциональных задач с ОП, техническим отделом и другими подразделениями
"""
    back_buttons = {"<- Назад": "competencies_back_to_types"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(technical_text, reply_markup=keyboard)


async def handle_competencies_management(callback: CallbackQuery):
    """Обработчик управленческих компетенций"""
    management_text = """
Развитие сотрудников
- Умение проводить оnе-to-one с C30
- Умение составлять ИПР для СЭО и экспертов оценщиков
- Умение оценивать компетенции кандидатов на СЗО

Влияние и коммуникация
- Готовность к сотрудничеству в команде руководителей смежных подразделений для достижения результата
- Знание последовательности работы при возникновении рекламации

Лидерство
- Готовность принимать на себя ответственность за результаты других
- Умение мотивировать людей и координировать их работу по достижению целей

Стратегическое мышление
- Знание целевых показателей компании по рынку и позиции относительно конкурентов
- Умение прогнозировать доходную и расходную части ОО
- Знание целевых показателей по стоимости склада
- Знание инструментов повышения ключевых показателей эффективности
- Знание инструментов управления расходами
"""
    back_buttons = {"<- Назад": "competencies_back_to_types"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(management_text, reply_markup=keyboard)


async def handle_competencies_back_to_types(callback: CallbackQuery):
    """Обработчик возврата к выбору типа компетенций"""
    competencies_text = """
Компетенции РОО, которые важны для работы
 и которые нужно развивать, можно разделить
 на 3 типа:
"""
    competencies_buttons = {
        "Корпоративные": "competencies_corporate",
        "Технические": "competencies_technical",
        "Управленческие": "competencies_management",
        "<- Назад": "back_to_main"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(competencies_buttons, interval=1)
    await callback.message.edit_text(competencies_text, reply_markup=keyboard)

