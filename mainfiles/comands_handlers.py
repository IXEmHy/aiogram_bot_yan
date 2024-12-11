from aiogram import types, F
from aiogram.types import ContentType
from aiogram.filters.command import Command

from config import PAYMENTS_TOKEN, HELP_COMMAND

from KeyboardsBot import *


# Объекты роутера, диспетчера, и бота
from bot_router_dp import *



from payments import *
from buymodul import PRICE

# Хэндлер на команду /buy
@dp.message(Command('buy'))
async def buy(message: types.Message):
    if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!")

    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://avatars.mds.yandex.net/i?id=969ec0afb38449ce98a60be3c9ddf8b8749a3424-10244736-images-thumbs&n=13",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать! "
        "Данный бот еще находится на стадии разработки. Но он будет связан с покукой подписки Yandex+\n"
        f"{HELP_COMMAND}", reply_markup=ikb)
        
# Хэндлер на команду /help
@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Этот бот пока что в разработке.", reply_markup=ikb)

# Милая проверка на отправку стиккера
@dp.message(F.content_type == ContentType.STICKER)
async def cmd_sticker(message: types.Message):
    await message.reply('Надеюсь, это милый стикер? К сожалению, я не могу его увидеить...')



# Автоответчик на события из инлайн клавиатуры(начинает обрабатываться когда пользователь нажмет на кнопку под сообщением)
@dp.callback_query()
async def callback_commands(callback: types.CallbackQuery):
    if callback.data == 'start':
        await callback.message.answer("Добро пожаловать! "
        "Данный бот еще находится на стадии разработки. Но он будет связан с покукой подписки Yandex+\n"
        , reply_markup=ikb)
    elif callback.data == "help":
        await callback.message.answer("Этот бот пока что в разработке.", reply_markup=ikb)
    elif callback.data == "buy":
        if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
            await callback.message.answer("Тестовый платеж!")

            await bot.send_invoice(callback.from_user.id,
                                title="Подписка на бота",
                                description="Активация подписки на бота на 1 месяц",
                                provider_token=PAYMENTS_TOKEN,
                                currency="rub",
                                photo_url="https://avatars.mds.yandex.net/i?id=969ec0afb38449ce98a60be3c9ddf8b8749a3424-10244736-images-thumbs&n=13",
                                photo_width=416,
                                photo_height=234,
                                photo_size=416,
                                is_flexible=False,
                                prices=[PRICE],
                                start_parameter="one-month-subscription",
                                payload="test-invoice-payload")
