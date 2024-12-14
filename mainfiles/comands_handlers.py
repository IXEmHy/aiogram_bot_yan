from aiogram import types, F
from aiogram.types import ContentType
from aiogram.filters.command import Command

from config import PAYMENTS_TOKEN, HELP_COMMAND

from KeyboardsBot import *


from aiogram import Router, Bot, types, F
from config import TOKEN_API
# Бот
bot = Bot(TOKEN_API)
# Роутер
router = Router()


from payments import *
from buymodul import PRICE



# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать! "
        "Данный бот еще находится на стадии разработки. Но он будет связан с покукой подписки Yandex+\n"
        f"{HELP_COMMAND}", reply_markup=ikb)
        
# Хэндлер на команду /help
@router.message(Command('help'))
async def cmd_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Этот бот пока что в разработке.", reply_markup=ikb)

# Хэндлер на команду /buy
@router.message(Command('buy'))
async def buy(message: types.Message):
    if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!")

    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://avatars.mds.yandex.net/get-music-misc/40584/img.625d332562b4b05f0dc6ec47/orig",
                           photo_width=2292,
                           photo_height=1200,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")

# Милая проверка на отправку стиккера
@router.message(F.content_type == ContentType.STICKER)
async def cmd_sticker(message: types.Message):
    await message.reply('Надеюсь, это милый стикер? К сожалению, я не могу его увидеить...')





# Автоответчик на события из инлайн клавиатуры(начинает обрабатываться когда пользователь нажмет на кнопку под сообщением)
@router.callback_query(F.data == 'start')
async def callback_start(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Добро пожаловать! "
        "Данный бот еще находится на стадии разработки. Но он будет связан с покукой подписки Yandex+\n", reply_markup=ikb)
    
@router.callback_query(F.data == 'help')
async def callback_start(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Этот бот пока что в разработке.", reply_markup=ikb)


@router.callback_query(F.data == 'buy')
async def callback_start(callback: types.CallbackQuery):
   if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await callback.answer()
        await callback.message.answer("Тестовый платеж!")

        await bot.send_invoice(callback.from_user.id,
                            title="Подписка на бота",
                            description="Активация подписки на бота на 1 месяц",
                            provider_token=PAYMENTS_TOKEN,
                            currency="rub",
                            photo_url="https://avatars.mds.yandex.net/get-music-misc/40584/img.625d332562b4b05f0dc6ec47/orig",
                            photo_width=2292,
                            photo_height=1200,
                            is_flexible=False,
                            prices=[PRICE],
                            start_parameter="one-month-subscription",
                            payload="test-invoice-payload")