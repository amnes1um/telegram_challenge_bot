from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def admin_panel_kb() -> InlineKeyboardMarkup:
    kd = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Рассылка", callback_data="mailing"))
    kb.add(InlineKeyboardButton(text="Статистика", callback_data="stats"))
    return kb

