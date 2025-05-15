from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command

from app.database.cart_db import db
from app.keyboards.menu_kb import *
from app.keyboards.kb_data import MENU_DATA

router = Router()
menu_kb = MenuKeyboard()

text_start = "🖐Добро пожаловать в онлайн магазин игрушек 'Вера'. Предлагаем выбрать игрушку из популярных категорий или просмотреть полный ассортимент"

@router.callback_query(F.data.startswith("levl_"))
async def handle_menu(callback: CallbackQuery):
    path = callback.data.replace("levl_", "")
    # 1. Находим текущий элемент в MENU_DATA
    current_item = next(
        (item for parent in MENU_DATA.values()
         for item in parent
         if item["callback_data"] == f"levl_{path}"),
        None
    )
    # 2. Получаем фото и текст
    photo = FSInputFile(current_item["photo"]) if current_item else None
    caption = current_item.get("caption", "Выберите раздел") if current_item else "Раздел"

    if photo:
        await callback.message.delete()
        await callback.message.answer_photo(photo=photo, caption=caption, reply_markup=menu_kb.build(path))
    else:
        await callback.message.delete()
        await callback.message.answer(
            text=caption,
            reply_markup=menu_kb.build(path))

        await callback.answer()


@router.callback_query(F.data.startswith("beck_"))
async def handle_back(callback: CallbackQuery):
    parent_path = callback.data.replace("beck_", "")  # "1.1"

    # 1. Находим родительский элемент
    parent_item = next(
        (item for level in MENU_DATA.values()
         for item in level
         if item["callback_data"] == f"levl_{parent_path}"),
        None
    )

    # 2. Получаем данные
    photo = FSInputFile(parent_item["photo"]) if parent_item else None
    caption = parent_item.get("caption", "Возврат") if parent_item else "Назад"

    if photo:
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=menu_kb.build(parent_path))
    else:
        await callback.message.delete()
        await callback.message.answer(
            text=text_start,
            reply_markup=menu_kb.build(parent_path))

    await callback.answer()


@router.callback_query(F.data.startswith("cart_"))
async def handle_back(callback: CallbackQuery):
    parent_path = callback.data.replace("cart_", "")  # "1.1"

    # 1. Находим родительский элемент
    parent_item = next(
        (item for level in MENU_DATA.values()
         for item in level
         if item["callback_data"] == f"levl_{parent_path}"),
        None
    )

    # 2. Получаем данные
    caption = parent_item.get("caption", "Возврат")
    await db.add_to_cart(callback.from_user.id, caption)
    await callback.answer("Товар добавлен в корзину")
