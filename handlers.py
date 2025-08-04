from aiogram import Router, types
from aiogram.filters import Command
from kb import admin_panel_kb
from config import admin_id
router = Router()

@router.message(Command("admin"))
async def admin(message: types.Message):
    if message.from_user.id == admin_id:
        keyboard = admin_panel_kb()
        await message.answer("Админ-панель", reply_markup=keyboard)
    else:
        pass

def register_handlers(dp):
    dp.include_router(router)
