# 🤖 FRESHBOT - Помощник руководителя отдела оценки

Telegram бот для поддержки руководителя отдела оценки компании FRESH в повседневной работе с командой, целями и процессами.

## 📝 Описание

FRESHBOT - это интеллектуальный помощник для руководителя отдела оценки компании FRESH. Бот помогает в роли:

🔥 **Лучшего специалиста** - развивает экспертизу  
🎯 **Играющего тренера** - обучает и мотивирует  
👨‍🏫 **Наставника** - передает опыт  
🔍 **Искателя кадров** - находит таланты  
🧠 **Психолога и мотиватора** - поддерживает команду  

Бот построен на aiogram 3.x с поддержкой современных возможностей.

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/v01cee/fresh_auto_info_neiro_bot.git
cd fresh_auto_info_neiro_bot
```

### 2. Настройка окружения
```bash
# Скопируйте файл с переменными окружения
cp env.example .env

# Отредактируйте .env файл, добавив ваш токен бота
# bot_token=your_bot_token_here
# admin_ids=123456789,987654321
```

### 3. Запуск бота
```bash
# Сборка и запуск через Docker
docker compose up -d --build

# Просмотр логов
docker compose logs -f bot

# Остановка
docker compose down
```

## 🛠️ Docker команды

```bash
# Сборка и запуск
docker compose up -d --build

# Просмотр логов
docker compose logs -f bot

# Остановка
docker compose down

# Перезапуск
docker compose restart bot
```

## 📁 Структура проекта

```
app/
├── __init__.py
├── bot.py                 # Основной файл бота
├── core/
│   ├── __init__.py
│   ├── config.py          # Конфигурация
│   ├── logging.py         # Настройка логирования
│   └── utils.py           # Утилиты
└── handlers/
    ├── __init__.py
    ├── start.py           # Обработчики стартовых команд
    └── admin.py           # Админские команды
```

## 🔧 Настройка

### Переменные окружения (.env)

```env
# Telegram Bot
bot_token=your_bot_token_here
admin_ids=123456789,987654321

# AI Service (DeepSeek)
deepseek_api_key=your_deepseek_api_key_here
ai_service_url=https://api.deepseek.com/v1

# Payment
payment_provider=yookassa
payment_shop_id=your_shop_id
payment_secret_key=your_secret_key

# App settings
debug=true
environment=development
```

## 🤖 Функции FRESHBOT

### 👥 **Работа с командой**
- Состав команды и роли
- Производительность сотрудников
- Развитие и обучение
- Поиск и подбор кадров

### 🎯 **Управление целями**
- Постановка целей для команды
- Отслеживание прогресса
- Анализ достижений
- Планирование задач

### 📈 **Управление процессами**
- Оптимизация рабочих процессов
- Документооборот
- Автоматизация рутины
- Контроль качества

### 🔥 **Мотивация команды**
- Создание мотивирующей среды
- Система поощрений
- Развитие карьеры
- Командная работа

### 📊 **Аналитика и отчетность**
- KPI команды
- Эффективность процессов
- Отчеты по проектам
- Анализ достижений

## 🐳 Развертывание на сервере

```bash
# 1. Клонирование на сервере
git clone https://github.com/v01cee/fresh_auto_info_neiro_bot.git
cd fresh_auto_info_neiro_bot

# 2. Настройка окружения
cp env.example .env
# Отредактируйте .env файл

# 3. Запуск в продакшене
docker compose up -d --build

# 4. Автозапуск при перезагрузке сервера
docker compose up -d --build --restart unless-stopped
```

## 📝 Лицензия

MIT License
