import httpx
import logging
from typing import Optional, Dict, Any
from core.config import settings

logger = logging.getLogger(__name__)


class AIService:
    """Сервис для работы с DeepSeek API"""
    
    def __init__(self):
        self.api_key = settings.deepseek_api_key
        self.api_url = f"{settings.ai_service_url}/chat/completions"
        self.model = "deepseek-chat"
    
    async def search_content(self, user_query: str, content_index: Dict[str, str]) -> Optional[str]:
        """
        Поиск контента по запросу пользователя
        
        Args:
            user_query: Запрос пользователя
            content_index: Словарь с индексами контента {ключ: описание}
        
        Returns:
            Ключ найденного контента или None
        """
        if not self.api_key:
            logger.warning("DeepSeek API ключ не настроен")
            return None
        
        # Формируем список всех вариантов для промпта
        content_options = "\n".join([
            f"{i+1}. {key} - {description}" 
            for i, (key, description) in enumerate(content_index.items())
        ])
        
        prompt = f"""Ты умный помощник для поиска информации в боте для руководителей отдела оценки и продаж компании FRESH Auto.

Пользователь задал запрос: "{user_query}"

Доступные варианты разделов бота (все возможные темы):

{content_options}

Твоя задача:
1. Внимательно проанализировать запрос пользователя
2. Понять суть запроса (о чем именно спрашивает пользователь)
3. Сравнить запрос со ВСЕМИ доступными вариантами выше
4. Найти наиболее релевантный раздел, который отвечает на вопрос пользователя
5. Вернуть ТОЛЬКО ключ выбранного варианта (например: "rop_functionality")

Важные правила и синонимы:
- РОП = Руководитель отдела продаж = РОП = руководитель продаж = начальник отдела продаж
- РОО = Руководитель отдела оценки = РОО = руководитель оценки = начальник отдела оценки
- ЭО = Эксперт-оценщик = оценщик = эксперт оценки
- МОП = Менеджер отдела продаж = менеджер продаж
- СМОП = Старший менеджер отдела продаж
- ППП = Предпродажная подготовка = предпродажка
- Классифайды = Avito, Auto.ru, drom.ru = рекламные площадки = объявления

Маппинг запросов на разделы:
- "функционал роп", "функции роп", "работа роп", "задачи роп", "распорядок роп", "график роп", "сценарий дня роп" → rop_functionality
- "функционал роо", "функции роо", "работа роо", "задачи роо", "распорядок роо", "график роо", "сценарий дня роо" → roo_functionality
- "компетенции", "навыки руководителя", "компетенции руководителя", "корпоративные компетенции", "технические компетенции", "управленческие компетенции" → roo_competencies
- "структура", "структура отделов", "структура компании", "отделы", "взаимодействие отделов", "какие отделы есть" → roo_structure
- "аналитика", "цифры", "работа с цифрами", "отчеты", "показатели", "метрики", "KPI", "статистика", "дашборды", "Qlik" → tasks_numbers
- "склад", "работа со складом", "управление складом", "контроль склада", "ценообразование", "скидки", "классифайды", "расстановка", "висяки", "переоценка", "аукцион", "10/10/10" → tasks_warehouse
- "клиент", "работа с клиентом", "клиенты", "заявки от клиентов" → tasks_client
- "персонал", "работа с персоналом", "сотрудники", "обучение персонала", "мотивация" → tasks_personnel
- "поставки", "работа с поставками", "закупки" → tasks_supplies
- "цели аналитики", "задачи аналитики" → analytics_goals
- "аналитика в действии", "как работает аналитика", "сбор данных", "обработка данных", "интерпретация", "действия на основе аналитики" → analytics_action
- "показатели", "KPI", "метрики", "индикаторы" → analytics_indicators
- "отчеты", "формы отчетности", "виды отчетов" → analytics_reports
- "ошибки аналитики", "проблемы с аналитикой", "типичные ошибки" → analytics_errors
- "Qlik", "система Qlik", "работа с Qlik" → analytics_qlik
- "ценообразование", "цена автомобиля", "установка цены", "выкупной", "комиссионный" → warehouse_pricing
- "скидки", "работа со скидками", "согласование скидки", "персональная скидка" → warehouse_discounts
- "контроль склада", "готовность склада", "расстановка автомобилей", "стандарты расстановки" → warehouse_control
- "классифайды", "Avito", "Auto.ru", "drom.ru", "продвижение на классифайдах", "поднятие объявлений" → warehouse_classifieds
- "управление складом", "контроль 45+", "висяки", "система 10/10/10", "повторная предпродажка", "переоценка склада", "аукцион" → warehouse_management

Формат ответа:
- Верни ТОЛЬКО ключ раздела (например: rop_functionality)
- БЕЗ кавычек, БЕЗ точек, БЕЗ дополнительных объяснений
- Если ни один вариант не подходит, верни: not_found

Примеры правильных ответов:
Запрос: "функционал роп" → rop_functionality
Запрос: "как работает роп" → rop_functionality
Запрос: "график дня руководителя продаж" → rop_functionality
Запрос: "функции роо" → roo_functionality
Запрос: "компетенции" → roo_competencies
Запрос: "структура отделов" → roo_structure
Запрос: "работа с цифрами" → tasks_numbers
Запрос: "аналитика" → tasks_numbers
Запрос: "склад" → tasks_warehouse
Запрос: "ценообразование" → warehouse_pricing
Запрос: "скидки" → warehouse_discounts
Запрос: "классифайды" → warehouse_classifieds
Запрос: "висяки" → warehouse_management
Запрос: "система 10/10/10" → warehouse_management
Запрос: "Qlik" → analytics_qlik

Верни только ключ:"""

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    self.api_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": self.model,
                        "messages": [
                            {
                                "role": "system",
                                "content": "Ты помощник для поиска информации. Отвечай только ключом раздела или 'not_found'."
                            },
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        "temperature": 0.3,
                        "max_tokens": 50
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    result = data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
                    
                    # Очищаем результат от кавычек и лишних символов
                    result = result.strip('"\'`').strip()
                    
                    # Проверяем, что результат есть в индексе контента
                    if result in content_index:
                        logger.info(f"AI поиск: запрос '{user_query}' → результат '{result}'")
                        return result
                    elif result == "not_found":
                        logger.info(f"AI поиск: запрос '{user_query}' → ничего не найдено")
                        return None
                    else:
                        # Пытаемся найти ключ в результате (на случай если AI добавил пояснения)
                        for key in content_index.keys():
                            if key in result:
                                logger.info(f"AI поиск: запрос '{user_query}' → найден ключ '{key}' в ответе '{result}'")
                                return key
                        logger.warning(f"AI поиск: запрос '{user_query}' → неизвестный результат '{result}'")
                        return None
                else:
                    logger.error(f"Ошибка API DeepSeek: {response.status_code} - {response.text}")
                    return None
                    
        except Exception as e:
            logger.error(f"Ошибка при запросе к DeepSeek API: {e}")
            return None


# Глобальный экземпляр сервиса
ai_service = AIService()

