import asyncio
from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def start_command(message: Message):
    """Обработчик команды /start"""
    username = message.from_user.username or "Пользователь"
    
    welcome_text = f"""
👋 Добро пожаловать, {username}!

Я FRESHBOT - ваш помощник в повседневной работе с командой, целями и процессами!

🔥 Как руководитель отдела оценки компании FRESH, вы:
• Лучший специалист
• Эксперт по продукту  
• Играющий тренер
• Наставник
• Искатель кадров
• Психолог и мотиватор

Но даже сильному лидеру и профессионалу порой нужна поддержка!
Поэтому я здесь, чтобы помочь вам! 😊

Выберите действие из меню ниже:
"""
    
    await message.answer(welcome_text)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Отправляем новое сообщение с инлайн-клавиатурой
    delayed_text = "Выберите раздел который тебя интересует и FRESHBOT тебе поможет!"
    keyboard_templates = KeyboardTemplates()
    delayed_keyboard = await keyboard_templates.get_delayed_keyboard()
    await message.answer(delayed_text, reply_markup=delayed_keyboard)


async def help_command(message: Message):
    """Обработчик команды /help"""
    help_text = """
📖 Помощь по боту:

/start - Начать работу с ботом
/help - Показать это сообщение
/info - Информация о боте

Для получения помощи обратитесь к администратору.
"""
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_cancel_keyboard()
    await message.answer(help_text, reply_markup=keyboard)


async def info_command(message: Message):
    """Обработчик команды /info"""
    info_text = """
ℹ️ Информация о боте:

🤖 Название: Fresh Auto Info Neiro Bot
📝 Описание: Бот для автоматической обработки информации с использованием нейросетей
🔧 Версия: 1.0.0
👨‍💻 Разработчик: v01cee
"""
    keyboard_templates = KeyboardTemplates()
    keyboard = await keyboard_templates.get_cancel_keyboard()
    await message.answer(info_text, reply_markup=keyboard)


async def handle_callback_queries(callback: CallbackQuery):
    """Обработчик всех callback запросов"""
    print(f"DEBUG: Обработчик callback вызван! Данные: {callback.data}")  # Отладочный лог
    keyboard_templates = KeyboardTemplates()
    
    match callback.data:
        case "roo_structure":
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
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(structure_text, reply_markup=keyboard)
            
        case "roo_functionality":
            functionality_text = """
Функционал РОО

Выберите направление работы:
"""
            functionality_buttons = {
                "Работа с поставками": "functionality_supplies",
                "Работа с клиентом": "functionality_client", 
                "Работа со складом": "functionality_warehouse",
                "Работа с цифрами": "functionality_numbers",
                "Работа с персоналом": "functionality_personnel"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(functionality_buttons, interval=1)
            await callback.message.edit_text(functionality_text, reply_markup=keyboard)
            
        case "roo_competencies":
            competencies_text = """
Компетенции РОО, которые важны для работы и которые нужно развивать, можно разделить на 3 типа:

1. КОРПОРАТИВНЫЕ КОМПЕТЕНЦИИ:
• Уважение к сотрудникам и клиентам - способность понимать и удовлетворять потребности клиентов
• Нацеленность на результат - способность достигать целей и демонстрировать высокий уровень качества работы
• Постоянное обучение и развитие - готовность совершенствовать себя и свою работу
• Командность - способность успешно работать с другими сотрудниками компании, достигая согласованных действий для реализации целей компании
• Ответственность - способность адекватно отвечать за то, что было ему поручено или что он взял на себя
• Способность к трансформациям - готовность быстро, открыто и гибко изменять свой образ жизни и профессиональную деятельность в ответ на изменения окружающей среды

2. ТЕХНИЧЕСКИЕ КОМПЕТЕНЦИИ:
• Работа с ценообразованием:
  - Знание качественной категоризации и ликвидности автомобилей
  - Знание элементов финального ценообразования (инвестиции, состояние, рынок, прогнозируемая прибыльность, количество ДТП, история)
  - Умение управлять консигнационным складом
  - Умение управлять "Склад 45+" - своевременная работа со складским ценообразованием
  - Навык контроля качества звонков, регулярности взаимодействия с консигнантом, состояния консигнационных автомобилей

• Работа с показателями и отчетностью:
  - Умение анализировать показатели эффективности РОО и выявлять зоны внимания
  - Умение прогнозировать и планировать операционные показатели РОО на будущие периоды
  - Умение формировать отчетность РОО и вести табели

• Работа со смежными подразделениями:
  - Умение анализировать ключевые показатели эффективности смежных подразделений
  - Знание кросс-функциональных задач с Отделом продаж, Техническим отделом и другими подразделениями

3. УПРАВЛЕНЧЕСКИЕ КОМПЕТЕНЦИИ:
• Развитие сотрудников:
  - Умение проводить встречи один-на-один с С30
  - Умение создавать Индивидуальные планы развития (ИПР) для старших экспертов по оценке и экспертов по оценке
  - Умение оценивать компетенции кандидатов на должность старшего эксперта по оценке

• Влияние и коммуникация:
  - Готовность к сотрудничеству в команде менеджеров из смежных подразделений для достижения результатов
  - Знание последовательности работы при возникновении жалобы

• Лидерство:
  - Готовность брать на себя ответственность за результаты других
  - Умение мотивировать людей и координировать их работу для достижения целей

• Стратегическое мышление:
  - Знание целевых показателей компании на рынке и ее позиции относительно конкурентов
  - Умение прогнозировать доходную и расходную части РОО
  - Знание целевых показателей по стоимости склада
  - Знание инструментов улучшения ключевых показателей эффективности
  - Знание инструментов управления расходами
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(competencies_text, reply_markup=keyboard)
            
        case "back_to_main":
            main_text = "Выберите раздел который тебя интересует и FRESHBOT тебе поможет!"
            keyboard = await keyboard_templates.get_delayed_keyboard()
            await callback.message.edit_text(main_text, reply_markup=keyboard)
            
        # Обработчики для функционала РОО
        case "functionality_supplies":
            supplies_text = """
Работа с поставками

• Контроль качества поступающих автомобилей
• Взаимодействие с поставщиками
• Планирование поставок
• Оценка ликвидности поставляемых автомобилей
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(supplies_text, reply_markup=keyboard)
            
        case "functionality_client":
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
                "Контроль отработки заявок от КЦ": "client_call_center"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(client_buttons, interval=1)
            await callback.message.edit_text(client_text, reply_markup=keyboard)
            
        case "functionality_warehouse":
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
                "Контроль качества сделанной предпродажной подготовки": "warehouse_pre_sale_quality"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(warehouse_buttons, interval=1)
            await callback.message.edit_text(warehouse_text, reply_markup=keyboard)
            
        case "functionality_numbers":
            numbers_text = """
Работа с цифрами

Выберите обязанность:
"""
            numbers_buttons = {
                "Обязанность 2.1": "numbers_duty_2_1",
                "Обязанность 2.2": "numbers_duty_2_2"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(numbers_buttons, interval=1)
            await callback.message.edit_text(numbers_text, reply_markup=keyboard)
            
        case "functionality_personnel":
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
                "Подбор персонала": "personnel_recruitment"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(personnel_buttons, interval=1)
            await callback.message.edit_text(personnel_text, reply_markup=keyboard)
            
        # Обработчики для работы с клиентом
        case "client_calls":
            calls_text = """
Контроль качества отработки входящих звонков

• Мониторинг времени ответа на звонки
• Контроль качества консультаций
• Анализ обращений клиентов
• Обучение операторов стандартам работы
• Ведение статистики звонков
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(calls_text, reply_markup=keyboard)
            
        case "client_website":
            website_text = """
Контроль отработки заявок с сайта

• Мониторинг поступления заявок
• Контроль времени обработки заявок
• Качество ответов на заявки
• Отслеживание конверсии заявок в сделки
• Анализ эффективности онлайн-каналов
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(website_text, reply_markup=keyboard)
            
        case "client_crm_entry":
            crm_entry_text = """
Контроль занесения клиента в CRM

• Проверка полноты данных о клиенте
• Контроль корректности заполнения полей
• Мониторинг своевременности внесения данных
• Анализ качества ведения клиентской базы
• Обучение сотрудников работе с CRM
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(crm_entry_text, reply_markup=keyboard)
            
        case "client_crm_consignor":
            crm_consignor_text = """
Контроль ведения комитента в CRM

• Отслеживание статусов комитентов
• Контроль обновления информации
• Мониторинг взаимодействия с комитентами
• Анализ эффективности работы с комитентами
• Планирование работы с комитентской базой
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(crm_consignor_text, reply_markup=keyboard)
            
        case "client_outgoing_calls":
            outgoing_calls_text = """
Контроль качества исходящих звонков

• Мониторинг инициативы в обзвоне клиентов
• Контроль соблюдения скриптов общения
• Анализ результативности исходящих звонков
• Обучение сотрудников техникам продаж
• Ведение статистики конверсии звонков
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(outgoing_calls_text, reply_markup=keyboard)
            
        case "client_documents":
            documents_text = """
Контроль корректно оформленных документов

• Проверка полноты документооборота
• Контроль соответствия документов стандартам
• Мониторинг своевременности оформления
• Анализ качества документооборота
• Обучение сотрудников правилам документооборота
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(documents_text, reply_markup=keyboard)
            
        case "client_payments":
            payments_text = """
Контроль соблюдения сроков оплаты клиентам и партнерам

• Мониторинг сроков выплат клиентам
• Контроль платежей партнерам
• Отслеживание дебиторской задолженности
• Анализ финансовой дисциплины
• Планирование денежных потоков
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(payments_text, reply_markup=keyboard)
            
        case "client_closing_manager":
            closing_manager_text = """
Работа в роли закрывающего менеджера

Выберите цель:
"""
            closing_manager_buttons = {
                "Цель: повышение конверсии": "closing_conversion",
                "Цель: предотвращение конфликтных ситуаций": "closing_conflicts"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(closing_manager_buttons, interval=1)
            await callback.message.edit_text(closing_manager_text, reply_markup=keyboard)
            
        case "client_complaints":
            complaints_text = """
Отработка рекламаций

• Прием и регистрация жалоб клиентов
• Анализ причин возникновения рекламаций
• Разработка планов устранения недостатков
• Контроль выполнения мероприятий
• Взаимодействие с ответственными подразделениями
• Мониторинг удовлетворенности клиентов
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(complaints_text, reply_markup=keyboard)
            
        case "client_call_center":
            call_center_text = """
Контроль отработки заявок от КЦ

Выберите направление:
"""
            call_center_buttons = {
                "Взаимодействие с КЦ": "call_center_interaction",
                "Контроль ЭО": "call_center_evaluation"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(call_center_buttons, interval=1)
            await callback.message.edit_text(call_center_text, reply_markup=keyboard)
            
        # Обработчики для закрывающего менеджера
        case "closing_conversion":
            await callback.message.edit_text("Пока нечего")
            
        case "closing_conflicts":
            await callback.message.edit_text("Пока нечего")
            
        case "call_center_interaction":
            await callback.message.edit_text("Пока нечего")
            
        case "call_center_evaluation":
            await callback.message.edit_text("Пока нечего")
            
        # Обработчики для работы со складом
        case "warehouse_pricing_new_arrival":
            await callback.message.edit_text("Пока нечего")
            
        case "warehouse_advertising":
            await callback.message.edit_text("Пока нечего")
            
        case "warehouse_check_new_arrival":
            await callback.message.edit_text("Пока нечего")
            
        case "warehouse_status_control":
            await callback.message.edit_text("Пока нечего")
            
        case "warehouse_problematic":
            await callback.message.edit_text("Пока нечего")
            
        case "warehouse_average_age":
            await callback.message.edit_text("Пока нечего")
            
        case "warehouse_pre_sale_quality":
            pre_sale_text = """
Контроль качества сделанной предпродажной подготовки

Выберите тип склада:
"""
            pre_sale_buttons = {
                "Выкупной склад": "warehouse_buyout",
                "Комиссионный склад": "warehouse_consignment",
                "Склад 45+": "warehouse_45_plus"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(pre_sale_buttons, interval=1)
            await callback.message.edit_text(pre_sale_text, reply_markup=keyboard)
            
        # Обработчики для типов складов
        case "warehouse_buyout":
            await callback.message.edit_text("Пока нечего")
            
        case "warehouse_consignment":
            await callback.message.edit_text("Пока нечего")
            
        case "warehouse_45_plus":
            await callback.message.edit_text("Пока нечего")
            
        # Обработчики для работы с цифрами
        case "numbers_duty_2_1":
            await callback.message.edit_text("Пока нечего")
            
        case "numbers_duty_2_2":
            await callback.message.edit_text("Пока нечего")
            
        # Обработчики для работы с персоналом
        case "personnel_intern_adaptation":
            await callback.message.edit_text("Пока нечего")
            
        case "personnel_burnout":
            await callback.message.edit_text("Пока нечего")
            
        case "personnel_motivation":
            await callback.message.edit_text("Пока нечего")
            
        case "personnel_training":
            await callback.message.edit_text("Пока нечего")
            
        case "personnel_dismissal":
            dismissal_text = """
Как говорит Денис Мигаль, с неэффективными нужно прощаться быстро. Ведь наименьшие потери - быстрые потери.

Но как понять что сотрудник точно неэффективен?

Когда мы дали ему обратную связь, что именно нас не устраивает в его работе и когда провели разбор и обучение.
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(dismissal_text, reply_markup=keyboard)
            
        case "personnel_recruitment":
            recruitment_text = """
Умение правильно подобрать людей в свою команду это одна из важнейших задач РОО. Для этого нужно создать потрет кандидата, настроить вакансию и правильно провести собеседование.

Выберите направление:
"""
            recruitment_buttons = {
                "Вакансия": "recruitment_vacancy",
                "Кого мы ищем": "recruitment_profile",
                "Как проводить собеседование": "recruitment_interview"
            }
            keyboard = await keyboard_templates.keyboard_ops.create_keyboard(recruitment_buttons, interval=1)
            await callback.message.edit_text(recruitment_text, reply_markup=keyboard)
            
        # Обработчики для подбора персонала
        case "recruitment_vacancy":
            vacancy_text = """
Проверить описание вакансии. она должна быть оформлена в корпоративном стиле (шаблон у HR менеджера).

Вакансия должна:
• Презентовать компанию
• Презентовать вакансию
• Побуждать к действию
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(vacancy_text, reply_markup=keyboard)
            
        case "recruitment_profile":
            profile_text_1 = """
Мы ищем доброжелательного и располагающего к общению человека!

• Располагающий образ (у такого хочется купить)
• Способность доносить мысли
• Желание работать с людьми (не боится людей, получает удовольствие от диалога)
• Готовность изучать новое (процедуры, регламенты, программы)
• Способность работать на компьютере
• Инициативный (Про активная жизненная позиция)
"""
            await callback.message.edit_text(profile_text_1)
            
            # Задержка 3 секунды
            await asyncio.sleep(3)
            
            profile_text_2 = """
Дополнительные требования:
• Опыт работы в продажах приветствуется
• Знание автомобильной тематики будет плюсом
• Готовность к обучению и развитию
• Коммуникабельность и стрессоустойчивость
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(profile_text_2, reply_markup=keyboard)
            
        case "recruitment_interview":
            interview_text_1 = """
Важно понимать, что собеседование это продажа. Продажа вакансии, себя как адекватного руководителя, компании.

Как любые продажи, собеседование можно разбить на этапы:

Small Talk
Этот этап помогает снять напряжённость и стресс в котором безусловно находится кандидат. Обозначить, что на собеседовании не будет правильных и не правильных ответов и точно не будет тестов. Что собеседование будет проходить в формате простой беседы

Расскажите о себе то, что вы считаете мне важно знать о Вас при приеме на работу

На этом этапе наша задача дать кандидату возможность рассказать о себе, вовлекаться в диалог, давать одобрительную оценку его рассказу. Цель: узнать о потребностях кандидата через диалог и вопросы! На основе этих потребностей мы будем строить нашу презентацию.
"""
            await callback.message.edit_text(interview_text_1)
            
            # Задержка 3 секунды
            await asyncio.sleep(3)
            
            interview_text_2 = """
Продажа вакансии, себя и компании
На этом этапе, используя полученную информацию, мы рассказываем о компании и вакансии. Акцентирую внимание на том что важно кандидату. Это может быть удобное расположение салона, узнаваемый бренд, наличие гоночной команды, надежность работодателя и т.д. И конечно презентуем себя.
"""
            keyboard = await keyboard_templates.get_cancel_keyboard()
            await callback.message.edit_text(interview_text_2, reply_markup=keyboard)
    
    await callback.answer()


def register_start_handlers(dp: Dispatcher):
    """Регистрация обработчиков стартовых команд"""
    dp.message.register(start_command, CommandStart())
    dp.message.register(help_command, Command("help"))
    dp.message.register(info_command, Command("info"))
    dp.callback_query.register(handle_callback_queries)
