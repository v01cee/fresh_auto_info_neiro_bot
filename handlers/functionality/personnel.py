import asyncio
from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_functionality_personnel(callback: CallbackQuery):
    """Обработчик меню работы с персоналом"""
    personnel_text = """
Работа с персоналом

Выберите направление:
"""
    personnel_buttons = {
        "Адаптация стажера": "personnel_intern_adaptation",
        "Работа с выгоранием": "personnel_burnout",
        "Мотивация": "personnel_motivation",
        "Обучение": "personnel_training",
        "Увольнение": "personnel_dismissal",
        "Подбор персонала": "personnel_recruitment",
        "<- Назад": "back_to_functionality"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(personnel_buttons, interval=1)
    await callback.message.edit_text(personnel_text, reply_markup=keyboard)


async def handle_personnel_intern_adaptation(callback: CallbackQuery):
    """Обработчик адаптации стажера"""
    back_buttons = {"<- Назад": "back_to_personnel_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_personnel_burnout(callback: CallbackQuery):
    """Обработчик работы с выгоранием"""
    back_buttons = {"<- Назад": "back_to_personnel_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_personnel_motivation(callback: CallbackQuery):
    """Обработчик мотивации"""
    back_buttons = {"<- Назад": "back_to_personnel_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_personnel_training(callback: CallbackQuery):
    """Обработчик обучения"""
    back_buttons = {"<- Назад": "back_to_personnel_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text("В разработке", reply_markup=keyboard)


async def handle_personnel_dismissal(callback: CallbackQuery):
    """Обработчик увольнения"""
    dismissal_text = """
Как говорит Денис Мигаль, с неэффективными нужно прощаться быстро. Ведь наименьшие потери - быстрые потери.

Но как понять что сотрудник точно неэффективен?

Когда мы дали ему обратную связь, что именно нас не устраивает в его работе и когда провели разбор и обучение.
"""
    back_buttons = {"<- Назад": "back_to_personnel_menu"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(dismissal_text, reply_markup=keyboard)


async def handle_personnel_recruitment(callback: CallbackQuery):
    """Обработчик подбора персонала"""
    recruitment_text = """
Умение правильно подобрать людей в свою команду это одна из важнейших задач РОО. Для этого нужно создать потрет кандидата, настроить вакансию и правильно провести собеседование.

Выберите направление:
"""
    recruitment_buttons = {
        "Вакансия": "recruitment_vacancy",
        "Кого мы ищем": "recruitment_profile",
        "Как проводить собеседование": "recruitment_interview",
        "<- Назад": "back_to_personnel_menu"
    }
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(recruitment_buttons, interval=1)
    await callback.message.edit_text(recruitment_text, reply_markup=keyboard)


async def handle_recruitment_vacancy(callback: CallbackQuery):
    """Обработчик вакансии"""
    vacancy_text = """
Проверить описание вакансии. она должна быть оформлена в корпоративном стиле (шаблон у HR менеджера).

Вакансия должна:
• Презентовать компанию
• Презентовать вакансию
• Побуждать к действию
"""
    back_buttons = {"<- Назад": "back_to_recruitment"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(vacancy_text, reply_markup=keyboard)


async def handle_recruitment_profile(callback: CallbackQuery):
    """Обработчик профиля кандидата"""
    # Сначала выводим первое сообщение
    profile_text_1 = """
HR это инструмент в подборе персонала. Задача РОО
дать HR менеджеру чёткое описание критериев
кандидатов которые нам нужны исходя из ситуации в
отделе и потребностях в сотрудниках
"""
    await callback.message.answer(profile_text_1)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Затем выводим второе сообщение с кнопкой "Назад"
    profile_text_2 = """
Мы ищем доброжелательного
и располагающего
к общению человека!

• Располагающий образ (у такого хочется купить)
• Способность доносить мысли
• Желание работать с людьми (не боится людей, получает удовольствие от диалога)
• Готовность изучать новое (процедуры, регламенты, программы)
• Способность работать на компьютере
• Инициативный (Про активная жизненная позиция)
"""
    back_buttons = {"<- Назад": "back_to_recruitment"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.answer(profile_text_2, reply_markup=keyboard)


async def handle_recruitment_interview(callback: CallbackQuery):
    """Обработчик проведения собеседования"""
    # Сначала выводим первое сообщение
    interview_text_1 = """
Важно понимать, что
собеседование это продажа.
Продажа вакансии, себя как
адекватного руководителя,
компании.
"""
    await callback.message.answer(interview_text_1)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Затем выводим второе сообщение с кнопкой "Назад"
    interview_text_2 = """
Как любые продажи, собеседование можно разбить на этапы:

• Small Talk
Этот этап помогает снять напряжённость и стресс в котором безусловно находится кандидат. Обозначить, что на собеседовании не будет правильных и не правильных ответов и точно не будет тестов. Что собеседование будет проходить в формате простой беседы

• "Расскажите о себе то, что вы считаете мне важно знать о Вас при приеме на работу"
На этом этапе наша задача дать кандидату возможность рассказать о себе, вовлекаться в диалог, давать одобрительную оценку его рассказу. Цель: узнать о потребностях кандидата через диалог и вопросы! На основе этих потребностей мы будем строить нашу презентацию.

• Продажа вакансии, себя и компании
На этом этапе, используя полученную информацию, мы рассказываем о компании и вакансии. Акцентирую внимание на том что важно кандидату. Это может быть удобное расположение салона, узнаваемый бренд, наличие гоночной команды, надежность работодателя и т.д. И конечно презентуем себя.
"""
    back_buttons = {"<- Назад": "back_to_recruitment"}
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.answer(interview_text_2, reply_markup=keyboard)

