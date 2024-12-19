import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.methods import DeleteWebhook
from comands_handlers import router

from moduls import os, load_dotenv

from moduls import async_main


# Запуск процесса поллинга новых апдейтов
async def main():
    await async_main()
    dp = Dispatcher()
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN_API"))
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