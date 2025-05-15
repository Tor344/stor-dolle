from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from app.keyboards.kb_data import *
from aiogram.types import  FSInputFile
class MenuKeyboard:
    def __init__(self):
        self.builder = InlineKeyboardBuilder()

    def get_photo(self, level_path: str) -> FSInputFile:
        """Возвращает фото для текущего уровня"""
        if level_path == "1":  # Для главного меню фото не нужно
            return None
        parent_path = self._get_parent_path(level_path)
        for item in MENU_DATA.get(parent_path, []):
            if item["callback_data"] == f"levl_{level_path}":
                return FSInputFile(item["photo"])
        return None

    def build(self, level_path: str) -> InlineKeyboardMarkup:
        """Строим клавиатуру на основе текущего пути"""
        self.builder = InlineKeyboardBuilder()  # Очищаем билдер

        # 1. Добавляем основные кнопки текущего уровня
        current_level_buttons = MENU_DATA.get(level_path, [])
        for button in current_level_buttons:
            self.builder.button(
                text=button["text"],
                callback_data=button["callback_data"]
            )

        # 2. Добавляем кнопку "Назад" если это не главное меню
        if level_path != "1":
            parent_path = self._get_parent_path(level_path)
            self.builder.button(
                text="⬅️ Назад",
                callback_data=f"beck_{parent_path}"
            )
        # 3. Добавляем "В корзину" для последнего уровня
        if len(level_path.split('.')) == 4 or level_path  in ["1.2.2","1.2.3","1.3.1","1.3.2"]:  # Если это уровень 3 (1.1.1 и т.д.)
            self.builder.button(
                text="🛒 В корзину",
                callback_data=f"cart_{level_path}"
            )

        # Оптимальное расположение кнопок
        self.builder.adjust(1, repeat=True)

        return self.builder.as_markup()

    def _get_parent_path(self, path: str) -> str:
        """Получаем путь родителя (для кнопки Назад)"""
        parts = path.split('.')
        return '.'.join(parts[:-1])


# Пример использования:
# Создаем клавиатуру для главного меню
start_keyboard = MenuKeyboard().build("1")


# Создаем клавиатуру для "Куклы" (уровень 1.1)
dolls_keyboard = MenuKeyboard().build("1.1")

# Создаем клавиатуру для машин
car_keyboard = MenuKeyboard().build("1.2")

# Создаем клавиатуру для "Куклы" (уровень 1.1)
lego_keyboard = MenuKeyboard().build("1.3")

# Создаем клавиатуру для "Барби" (уровень 1.1.1)
barbie_keyboard = MenuKeyboard().build("1.1.1")

basket_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Удалить все товары",callback_data="delit")],
                                                        [InlineKeyboardButton(text="Подтвердить и оформить заказ",callback_data="reliability")]])

basket_start_keyboard = ReplyKeyboardMarkup(resize_keyboard= True,keyboard=[[KeyboardButton(text="Корзина")],[KeyboardButton(text="Тех.поддержка")]])

