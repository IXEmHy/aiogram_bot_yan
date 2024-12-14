import asyncio
import logging

from aiogram import Dispatcher
from aiogram.methods import DeleteWebhook
from comands_handlers import router, bot

dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Bot was running')
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")