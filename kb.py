from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def admin_panel_kb() -> InlineKeyboardMarkup:
    kd = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Рассылка", callback_data="mailing"))
    kb.add(InlineKeyboardButton(text="Статистика", callback_data="stats"))
    kb.add(InlineKeyboardButton(text="Выход", callback_data="exit"))
    return kb

def get_confirm_inline_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton("Да", callback_data="confirm_yes"))
    kb.add(InlineKeyboardButton("Нет", callback_data="confirm_no"))
    return kb
