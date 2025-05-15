from aiogram import Bot, Dispatcher
import config.settings as set
from app.start.handlers import router as start_router
from app.menu_handlers.handlers import router as user_router
from app.admin.handlers import router as admin_router
from app.basket.handlers import router as basket_router

bot = Bot(token=set.API_TOKEN)
dp = Dispatcher()


dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(start_router)
dp.include_router(basket_router)

if __name__ == "__main__":
    dp.run_polling(bot)