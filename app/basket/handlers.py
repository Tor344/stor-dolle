from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram import Bot

from config.settings import admin_id
from app.database.cart_db import db
from app.keyboards.menu_kb import *
from app.keyboards.kb_data import MENU_DATA

router = Router()
menu_kb = MenuKeyboard()

text_start = "🖐Добро пожаловать в онлайн магазин игрушек 'Вера'. Предлагаем выбрать игрушку из популярных категорий или просмотреть полный ассортимент"

@router.message(F.text == "Корзина")
async def basket(message:Message):
    data = list(await db.get_cart_items(message.from_user.id))
    if data == []:
        await message.answer("Корзина пуста")
        path = "1"
        await message.answer(
            text=text_start,
            reply_markup=menu_kb.build(path))

        return
    text = "Товары в корзине:\n"
    for i in data:
        text = text + i + ",\n"
    await message.answer(text,reply_markup=basket_keyboard)

@router.callback_query(F.data.startswith("delit"))
async def handle_menu(callback: CallbackQuery):
    await db.clear_cart(callback.from_user.id)
    path = "1"
    await callback.answer("Товары успешно удалены")

    await callback.message.edit_text(
        text=text_start,
        reply_markup=menu_kb.build(path))

    await callback.answer()


@router.callback_query(F.data.startswith("reliability"))
async def handle_menu(callback: CallbackQuery,bot:Bot):
    await callback.answer("Заказ создан")
    await callback.message.delete()
    await callback.message.answer(f"Заказ создан\n ID. {callback.from_user.id}\n Забрать товар вы можете по адресу: г. Азов, ул. Промышленная 2а")
    data = list(await db.get_cart_items(callback.from_user.id))
    text = "Товары в корзине:\n"
    for i in data:
        text = text + i + ",\n"
    await bot.send_message(
        chat_id=admin_id,

        text=f"🛒 Новый заказ от пользователя {callback.from_user.full_name} \n(ID: {callback.from_user.id} (@{callback.from_user.username})\n {text})"
    )
    await db.clear_cart(callback.from_user.id)
