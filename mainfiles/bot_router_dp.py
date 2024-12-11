from aiogram import Bot, Dispatcher, Router
from config import TOKEN_API
# Объект бота
bot = Bot(TOKEN_API)
# Диспетчер
dp = Dispatcher()
# Роутер
router = Router()