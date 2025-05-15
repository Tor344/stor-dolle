from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command


from app.keyboards.menu_kb import start_keyboard, basket_start_keyboard
router = Router()

text_start = "🖐Добро пожаловать в онлайн магазин игрушек 'Вера'. Предлагаем выбрать игрушку из популярных категорий или просмотреть полный ассортимент"


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("👋",reply_markup=basket_start_keyboard)
    await message.answer(text_start, reply_markup=start_keyboard,)

@router.message(F.text == "Тех.поддержка")
async def start(message: Message):
    await message.answer(f"Техподдержка: @V_E_R_Y_S")



