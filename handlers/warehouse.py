from aiogram.types import CallbackQuery
from core.keyboard_templates import KeyboardTemplates


async def handle_warehouse_pricing(callback: CallbackQuery):
    """Обработчик ценообразования нового поступления"""
    pricing_text = """Ценообразование нового поступления

Цель: сформировать конкурентную в рынке, справедливую для клиента цену с максимально возможной маржой для салона в условиях конкретного периода.

Работу с ценообразованием ведут руководители отделов продаж и оценки. РОП занимается ценообразованием выкупных автомобилей, а РОО – комиссионных.

Ценообразование основывается на истории продаж салона / компании, данных профильных аналитических платформ (в качестве рекомендации) и данных классифайдов (общая статистика).
"""
    keyboard_templates = KeyboardTemplates()
    pricing_buttons = {
        "Выкупной": "warehouse_pricing_purchase",
        "Комиссионный": "warehouse_pricing_commission",
        "<- Назад": "back_to_warehouse"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(pricing_buttons, interval=1)
    await callback.message.edit_text(pricing_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_discounts(callback: CallbackQuery):
    """Обработчик работы со скидками"""
    discounts_text = """РОП/СМОП перед согласованием персональной скидки клиенту на а/м должен получить от МОП подробный отчет по этому а/м и обращению клиента. МОП, в свою очередь, обязан подготовить отчет, обосновывая предоставление скидки на а/м на основании:

• полной презентации а/м клиенту; 
• результатов тест-драйва с клиентом;
• результатов осмотра а/м на подъемнике;
• анализа рынка;
• аргументов клиента, почему должна быть предоставлена скидка.

Также до обсуждения скидки на а/м с клиентом, МОП обязан проговорить с ним все выгоды приобретения а/м в нашем автосалоне, продать ценность покупки а/м в полную стоимость.
Только после прохождения всех этапов работы с клиентом и анализа отчета, предоставленного МОП, РОП/СМОП может согласовать скидку на а/м или подключиться к работе с клиентом, чтобы «дожать» сделку по полной стоимости.
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(discounts_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_control(callback: CallbackQuery):
    """Обработчик контроля состояния склада"""
    control_text = "Контроль состояния склада:"
    keyboard_templates = KeyboardTemplates()
    control_buttons = {
        "Оценка готовности склада": "warehouse_control_readiness",
        "Стандарты расстановки а\\м": "warehouse_control_placement",
        "<- Назад": "back_to_warehouse"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(control_buttons, interval=1)
    await callback.message.edit_text(control_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_classifieds(callback: CallbackQuery):
    """Обработчик работы с класифайдами"""
    classifieds_text = """Варианты продвижения автомобиля на классифайдах:

• поднятие а/м в топ публикаций
• реклама на отдельную позицию
• скидка на отдельную позицию
• рассылка в избранное

Решение о продвижении а/м принимает РОП на основе анализа обращений по автомобилю (звонков и визитов), позиции а/м среди всех предложений, анализа предложений у конкурентов либо если а/м попал в категорию «висяки».

Важно обращать внимание на время «поднятия» объявлений. Поднятие автомобиля на классифайде происходит на основании статистики времени просмотра объявлений пользователями, предоставляемой конкретным классифайдом (время может значительно отличаться по регионам).

Пользователь размещает автомобили через личный кабинет Fresh Auto с оплатой с собственного юридического лица. С Avito и Auto.ru заключается договор-оферта, с drom.ru заключается стандартный договор. Сопровождением процесса заключения договоров Пользователя занимается аккаунт-менеджер.

На продвижение а/м ежемесячно выделяется бонусная сумма от классифайда, на котором размещены а/м. Она зависит от объема выкладки авто на классифайды в предыдущем месяце.
РОП должен равномерно распределить бонусные средства на текущий месяц, с определенной периодичностью поднимая а/м в рекламном рейтинге. Частота поднятий в рейтинге будет зависеть от специфики конкретного региона.


РОО занимается продвижением а/м на интернет-площадке при отсутствии РОП.
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(classifieds_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management(callback: CallbackQuery):
    """Обработчик управления складом"""
    management_text = "Управление складом:"
    keyboard_templates = KeyboardTemplates()
    management_buttons = {
        "Выкупной": "warehouse_management_purchase",
        "Комиссионный": "warehouse_management_commission",
        "<- Назад": "back_to_warehouse"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(management_buttons, interval=1)
    await callback.message.edit_text(management_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_pricing_purchase(callback: CallbackQuery):
    """Обработчик ценообразования выкупного автомобиля"""
    purchase_text = """Выкупной

Исполнитель: РОП

Анализ рынка идентичных моделей (не менее 10 моделей) *
Определение среднерыночной стоимости
Установление цены на автомобиль на первые 10 дней:
 на 3-5% выше среднерыночной стоимости;
на 10% выше - при явных преимуществах автомобиля на фоне рынка на первые 10 дней)
Переоценка автомобиля по схеме 10/10/10**, где
во вторые 10 дней на основе анализа обращений по а/м и причин отказов указывать рыночную стоимость;
последние 10 дней продавать по цене ниже рыночной
*Анализ рынка идентичных моделей: по году выпуска; поколению; комплектации; пробегу; количеству ДТП; количеству собственников; общему состоянию
**10 – условный промежуток времени, который может изменяться в зависимости от обстоятельств.
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_pricing"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(purchase_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_pricing_commission(callback: CallbackQuery):
    """Обработчик ценообразования комиссионного автомобиля"""
    commission_text = """Комиссионный

Исполнитель: ЭО
Анализ рынка идентичных моделей*
Определение среднерыночной стоимости.
Установление цены. 
Комиссия должна составлять 5% от стоимости автомобиля, но не менее 70 000 р.
Согласование цены с комитентом 
Переоценка автомобиля каждую неделю (понижение до рыночной цены, если изначально автомобиль был выше рынка) с согласия комитента или корректировочные действия с самим автомобилем
*Анализ рынка идентичных моделей: по году выпуска; поколению; комплектации; пробегу; количеству ДТП; количеству собственников; общему состоянию
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_pricing"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(commission_text, reply_markup=keyboard)
    await callback.answer()


async def handle_back_to_warehouse_pricing(callback: CallbackQuery):
    """Обработчик возврата к ценообразованию"""
    await handle_warehouse_pricing(callback)


async def handle_warehouse_control_readiness(callback: CallbackQuery):
    """Обработчик оценки готовности склада"""
    readiness_text = """Для поддержания надлежащего внешнего вида а/м РОП взаимодействует со сток-
менеджером: контролирует сроки предпродажной подготовки а/м и готовности склада
к приему клиентов.

В случае если а/м не подготовлены вовремя, РОП/РОО оставляет комментарии в CRM, создавая
запрос на проведение работ по а/м. Задача ППП: в кратчайшие сроки произвести
все необходимые работы
по подготовке а/м.


Требования к готовности торговой площадки к приему клиентов:


·       территория площадки чистая, без мусора
·       автомобили чистые
·       автомобили выставлены согласно требованиям
·       на автомобилях присутствуют ценники с актуальными ценами
·       ценники целые, подномерные рамки и заглушки на месте
·       отсутствуют подтеки масла
·       автомобиль заправлен / аккумулятор заряжен – готов к тест-драйву.

Обход склада с проверкой готовности к приему клиентов проводится каждое

утро! Склад должен быть полностью готов до 11:00
"""
    await callback.message.edit_text(readiness_text)
    await callback.answer()


async def handle_warehouse_control_placement(callback: CallbackQuery):
    """Обработчик стандартов расстановки а/м"""
    placement_text = """Fresh уделяет расстановке автомобилей особое внимание. Поэтому автомобили на торговой площадке должны быть выставлены согласно правилам:
Автомобили должны быть расположены по классам.
В каждом сегменте автомобили расставляются по маркам / ценовым сегментам.
Автомобили корпоративных поставок одного цвета не рекомендуется выставлять в ряд рядом друг с другом. Необходимо ставить их рядом с другими а/м, максимум по два корпоративных образца рядом.
По возможности необходимо миксовать автомобили по цветам, чтобы рассеять внимание на всю торговую площадку.
Ряды из автомобилей должны быть ровными.
Автомобили на площадке должны быть чистыми. По регламенту мойка кузова должна производиться раз в три-четыре дня.
На каждом автомобиле должен быть ценник. Цена на автомобиль печатается из CRM и размещается на лобовом стекле автомобиля.
На «лицевой» ряд торговой площадки необходимо выставлять эксклюзивные а/м, которые способны привлечь внимание клиента.
Если площадка позволяет выставку а/м на фасадной части, то там может быть выставлен ликвидный модельный микс из а/м разного сегмента.
Рекомендуется размещение ликвидного склада разной категории на фасаде автосалона «лицом» к улице / дороге для привлечения большего внимания проходящего трафика
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_control"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(placement_text, reply_markup=keyboard)
    await callback.answer()


async def handle_back_to_warehouse_control(callback: CallbackQuery):
    """Обработчик возврата к контролю состояния склада"""
    await handle_warehouse_control(callback)


async def handle_warehouse_management_purchase(callback: CallbackQuery):
    """Обработчик управления выкупным складом"""
    purchase_text = "Здесь мы используем несколько инструментов управления и контроля"
    keyboard_templates = KeyboardTemplates()
    purchase_buttons = {
        "контроль 10\\10\\10": "warehouse_management_purchase_10_10_10",
        "Повторная предпродажка": "warehouse_management_purchase_reprep",
        "Контроль склада \"45+\"": "warehouse_management_purchase_45",
        "Переоценка склада": "warehouse_management_purchase_reprice",
        "В аукцион": "warehouse_management_purchase_auction",
        "<- Назад": "back_to_warehouse_management"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(purchase_buttons, interval=1)
    await callback.message.edit_text(purchase_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management_commission(callback: CallbackQuery):
    """Обработчик управления комиссионным складом"""
    import asyncio
    
    # Первое сообщение без кнопки
    commission_text = """Основной задачей РОО при работе с комиссионным складом является контроль работы ЭО"""
    await callback.message.edit_text(commission_text)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Второе сообщение
    control_text = """РОО контролирует:
• качество звонков комитенту
• регулярность взаимодействия с комитентом
• состояние автомобиля (если автомобиль не продается более 30 дней)"""
    await callback.message.answer(control_text)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Третье сообщение
    tasks_text = "Ключевые задачи эксперта-оценщика:"
    await callback.message.answer(tasks_text)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Отправляем фото
    photo_id = "AgACAgIAAxkBAAPIaRZhhjI3gpctvZCbfEgjokkg7s0AAv4Maxstl7lIqY6f2h0P2JoBAAMCAAN4AAM2BA"
    await callback.message.answer_photo(photo_id)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Четвертое сообщение
    decision_text = """Итоговое  решение  по  каждому  действию  с  автомобилем  принимается  клиентом.
Достигнутые договоренности фиксируются посредством SMS отправкой через CRM."""
    await callback.message.answer(decision_text)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Пятое сообщение с кнопкой "Назад"
    termination_text = """Если автомобиль не продается более 30 дней, а клиент отказывается снижать цену / улучшать состояние автомобиля РОО имеет право расторгнуть договор комиссии."""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_management"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.answer(termination_text, reply_markup=keyboard)
    
    await callback.answer()


async def handle_warehouse_management_purchase_10_10_10(callback: CallbackQuery):
    """Обработчик контроля 10/10/10"""
    text_10_10_10 = """Контроль движения автомобиля осуществляется по системе 10/10/10. Система предполагает работу с автомобилем при его задержке на складе. Сроки условны: могут быть 10/10/10 или 3/5/10 дней в зависимости от ситуации на рынке.
Последовательность действий:
Индивидуальный анализ каждого автомобиля в первые дни после поступления на склад, а затем через три/пять/десять дней по следующим критериям: количество звонков / количество визитов /сделки, количество отказов и их причины.
Если нет звонков, необходимо работать с ценой на автомобиль. Анализ рынка: сравнение объявления авто с объявлениями автомобилей - «одноклассников» в рынке, уточнение насколько данный автомобиль актуален в данном регионе. Снижение цены (при необходимости).
Если нет визитов, необходимо работать со звонками: прослушать все звонки по этому автомобилю, выяснить, в чем проблема, провести дополнительную презентацию автомобиля для менеджеров с разбором ошибок.
Если нет сделок, необходимо работать с автомобилем: проверить его карточку в CRM, выяснить у менеджеров отдела продаж недостатки автомобиля по мнению клиентов, отправить автомобиль на повторную предпродажную подготовку (при необходимости), провести повторную презентацию автомобиля отделу продаж.
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_management_purchase"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(text_10_10_10, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management_purchase_reprep(callback: CallbackQuery):
    """Обработчик повторной предпродажки"""
    reprep_text = """В случае, если просмотр автомобиля клиентами приводит к отказам от сделки или если автомобиль не продается в течение длительного времени (более 30 дней), РОП проводит личную оценку состояния автомобиля и может принять решение о дополнительной (повторной) предпродажной подготовке.
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_management_purchase"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(reprep_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management_purchase_auction(callback: CallbackQuery):
    """Обработчик продажи в аукцион"""
    auction_text = """Если автомобиль не продается в течение 90 дней, то после анализа состояния автомобиля, анализа рынка, работы с ценой и самим автомобилей, его рекомендуется продать через
«Аукцион» с фиксацией убытков.
"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_management_purchase"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(auction_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management_purchase_45(callback: CallbackQuery):
    """Обработчик контроля склада 45+"""
    import asyncio
    
    # Первое сообщение
    text_45_1 = """Машины которые задержались на складе и продаются более 45 дней, во FRESH называются "висяками". При этом его себестоимость на этих автомобилях зачастую равна или
превышает сумму продажи."""
    await callback.message.edit_text(text_45_1)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Второе сообщение
    text_45_2 = """Автомобиль становится «висяком», когда долго пребывает на складе, требуя определенных расходов на свое содержание (ФОТ сотрудников; содержание на площадке и обслуживание охрана, мойка, заправка); размещение на рекламных площадках; проценты на
стоимость заемных денег для выкупа а/м на площадку)."""
    await callback.message.answer(text_45_2)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Третье сообщение
    text_45_3 = """Например: 
Так, при сумме закупки 1 000 000 р. и наценке 100 000 р., при продаже а/м в этот же день рентабельность составит 100 000 р. При продаже через 2 недели при ставке 25% годовых
рентабельность составит 89 853 р., не считая расходов на содержание. При продаже а/м через месяц – 79 166 р., не считая расходов на содержание и т.д. Помимо всех вышеперечисленных расходов, а/м требует переоценки каждые 10 дней, соответственно, рентабельность будет снижаться еще больше при задержке а/м на складе."""
    await callback.message.answer(text_45_3)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Четвертое сообщение
    text_45_4 = "Поэтому важность контроля сроков продажи сложно переоценить."
    await callback.message.answer(text_45_4)
    
    # Задержка 3 секунды
    await asyncio.sleep(3)
    
    # Пятое сообщение с кнопкой "Назад"
    text_45_5 = """Если позиция зависла, РОП/РОО проводит анализ причин, влияющих на низкий спрос: ценообразование; тех. состояние а/м некачественная предпродажная подготовка а/м; отсутствие знаний менеджеров ОП данной позиции; отсутствие предложений МОП клиентам; несоответствующие фотографии а/м на классифайдах и др.

Выявив причину, РОП/РОО может предпринять определенные действия:

• если проблема с ценой (цена завышена), то дополнительно для клиента могут быть назначены спец.услуги: химчистка или полировка в подарок; бесплатное такси для клиента из салона; предложение ускоренного расчета с клиентом и пр. Также может быть назначена доп. скидка;
• если вопрос в тех. состоянии а/м, делается соответствующий запрос техкору;
• если вопрос в ППП, РОП/РОО делает запрос в отдел ППП для устранения недочетов;
• если недочеты в работе персонала, РОП/РОО работает с сотрудниками — проводится дополнительный тренинг, повторная презентация а/м. Также сотрудникам может быть назначен материальный бонус (дополнительная премия) или НЕматериальный спец.бонус за продажу «висяка» (назначить статусную задачу; отпустить раньше с работы и пр.)
• при обнаружении несоответствующих фотографий на классифайдах, РОП/РОО обращается за решением задачи к контент-менеджерам. СЕЗОННОСТЬ ФОТОГРАФИЙ; ШИНОМОНТАЖ лето/зима

Если выкупной автомобиль не продается более 45 дней в своей локации, то РОП может оценить уровень спроса на данную модель автомобиля в своем регионе и регионах присутствия Fresh Auto, и предложить РОПу другой локации переместить авто между складами."""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_management_purchase"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.answer(text_45_5, reply_markup=keyboard)
    
    await callback.answer()


async def handle_warehouse_management_purchase_reprice(callback: CallbackQuery):
    """Обработчик переоценки склада"""
    reprice_text = """РОП проводит анализ рынка и обращений по каждому выкупному а/м и принимает решение о понижении/повышении цены"""
    keyboard_templates = KeyboardTemplates()
    reprice_buttons = {
        "Нет обращений": "warehouse_management_purchase_reprice_no_calls",
        "Есть обращения": "warehouse_management_purchase_reprice_has_calls",
        "<- Назад": "back_to_warehouse_management_purchase"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(reprice_buttons, interval=1)
    await callback.message.edit_text(reprice_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management_purchase_reprice_no_calls(callback: CallbackQuery):
    """Обработчик переоценки при отсутствии обращений"""
    no_calls_text = """Переоценка (снижение цены) согласно текущему положению на рынке на дату"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_management_purchase_reprice"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(no_calls_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management_purchase_reprice_has_calls(callback: CallbackQuery):
    """Обработчик переоценки при наличии обращений"""
    has_calls_text = "Тут важно понять"
    keyboard_templates = KeyboardTemplates()
    has_calls_buttons = {
        "Много обращений": "warehouse_management_purchase_reprice_many_calls",
        "Мало обращений": "warehouse_management_purchase_reprice_few_calls",
        "<- Назад": "back_to_warehouse_management_purchase_reprice"
    }
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(has_calls_buttons, interval=1)
    await callback.message.edit_text(has_calls_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management_purchase_reprice_many_calls(callback: CallbackQuery):
    """Обработчик переоценки при большом количестве обращений"""
    many_calls_text = """Анализ комментариев МОП в CRM, проверка а/м вживую и принятие мер (разбор ошибок/недоработок  МОП;  повторная предпродажная подготовка а/м и т.д.)"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_management_purchase_reprice_has_calls"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(many_calls_text, reply_markup=keyboard)
    await callback.answer()


async def handle_warehouse_management_purchase_reprice_few_calls(callback: CallbackQuery):
    """Обработчик переоценки при малом количестве обращений"""
    few_calls_text = """Переоценка хотя бы на 1 000 р., чтобы клиенты, добавившие а/м
в избранное, получили оповещение"""
    keyboard_templates = KeyboardTemplates()
    back_buttons = {"<- Назад": "back_to_warehouse_management_purchase_reprice_has_calls"}
    keyboard = await keyboard_templates.keyboard_ops.create_keyboard(back_buttons, interval=1)
    await callback.message.edit_text(few_calls_text, reply_markup=keyboard)
    await callback.answer()


async def handle_back_to_warehouse_management_purchase_reprice_has_calls(callback: CallbackQuery):
    """Обработчик возврата к меню 'Есть обращения'"""
    await handle_warehouse_management_purchase_reprice_has_calls(callback)


async def handle_back_to_warehouse_management_purchase_reprice(callback: CallbackQuery):
    """Обработчик возврата к переоценке склада"""
    await handle_warehouse_management_purchase_reprice(callback)


async def handle_back_to_warehouse_management_purchase(callback: CallbackQuery):
    """Обработчик возврата к управлению выкупным складом"""
    await handle_warehouse_management_purchase(callback)


async def handle_back_to_warehouse_management(callback: CallbackQuery):
    """Обработчик возврата к управлению складом"""
    await handle_warehouse_management(callback)


async def handle_back_to_warehouse(callback: CallbackQuery):
    """Обработчик возврата к меню работы со складом"""
    from handlers.tasks import handle_tasks_warehouse
    await handle_tasks_warehouse(callback)

