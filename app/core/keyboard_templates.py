from app.core.keyboards import KeyboardOperations


class KeyboardTemplates:
    """Готовые шаблоны клавиатур для бота"""
    
    def __init__(self):
        self.keyboard_ops = KeyboardOperations()
    
    async def get_main_menu(self):
        """Главное меню FRESHBOT"""
        buttons = {
            "👥 Команда": "team",
            "🎯 Цели": "goals", 
            "📈 Процессы": "processes",
            "🔥 Мотивация": "motivation",
            "📊 Аналитика": "analytics",
            "⚙️ Настройки": "settings"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_admin_menu(self):
        """Админское меню"""
        buttons = {
            "👥 Пользователи": "admin_users",
            "📊 Статистика": "admin_stats", 
            "📢 Рассылка": "admin_broadcast",
            "⚙️ Настройки": "admin_settings",
            "🔙 Назад": "back_to_main"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_team_menu(self):
        """Меню работы с командой"""
        buttons = {
            "👥 Состав команды": "team_roster",
            "📊 Производительность": "team_performance", 
            "🎓 Развитие": "team_development",
            "🔍 Поиск кадров": "team_recruitment",
            "🔙 Назад": "back_to_main"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_goals_menu(self):
        """Меню управления целями"""
        buttons = {
            "🎯 Постановка целей": "goals_setting",
            "📈 Отслеживание": "goals_tracking", 
            "📊 Анализ": "goals_analysis",
            "📋 Планирование": "goals_planning",
            "🔙 Назад": "back_to_main"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_processes_menu(self):
        """Меню управления процессами"""
        buttons = {
            "⚙️ Оптимизация": "processes_optimization",
            "📋 Документооборот": "processes_documents", 
            "🔄 Автоматизация": "processes_automation",
            "📊 Контроль": "processes_control",
            "🔙 Назад": "back_to_main"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_motivation_menu(self):
        """Меню мотивации"""
        buttons = {
            "💪 Мотивирующая среда": "motivation_environment",
            "🏆 Система поощрений": "motivation_rewards", 
            "📈 Развитие карьеры": "motivation_career",
            "🤝 Командная работа": "motivation_teamwork",
            "🔙 Назад": "back_to_main"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_analytics_menu(self):
        """Меню аналитики"""
        buttons = {
            "📈 KPI команды": "analytics_kpi",
            "📊 Эффективность": "analytics_efficiency", 
            "📋 Отчеты": "analytics_reports",
            "🎯 Достижения": "analytics_achievements",
            "🔙 Назад": "back_to_main"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_settings_menu(self):
        """Меню настроек FRESHBOT"""
        buttons = {
            "🔔 Уведомления": "settings_notifications",
            "🌐 Язык": "settings_language",
            "🔒 Приватность": "settings_privacy",
            "📱 Персонализация": "settings_personalization",
            "🔙 Назад": "back_to_main"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_yes_no_keyboard(self):
        """Клавиатура Да/Нет"""
        buttons = {
            "✅ Да": "yes",
            "❌ Нет": "no"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=2)
    
    async def get_cancel_keyboard(self):
        """Клавиатура с кнопкой Отмена"""
        buttons = {
            "❌ Отмена": "cancel"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=1)
    
    async def get_reply_keyboard(self):
        """Обычная клавиатура"""
        buttons = ["📱 Главное меню", "ℹ️ Информация", "🆘 Помощь"]
        return await self.keyboard_ops.create_keyboard(buttons, interval=1)
    
    async def get_delayed_keyboard(self):
        """Клавиатура для отложенного сообщения"""
        buttons = {
            "РОО в структуре компании": "roo_structure",
            "Функционал РОО": "roo_functionality", 
            "Компетенции РОО": "roo_competencies"
        }
        return await self.keyboard_ops.create_keyboard(buttons, interval=3)
