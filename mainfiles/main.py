import asyncio
from aiogram.methods import DeleteWebhook
from comands_handlers import *


# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    await bot(DeleteWebhook(drop_pending_updates=True))

if __name__ == "__main__":
    print('Bot was running')
    asyncio.run(main())
    print('Bot was stopped')
    
    
    
    