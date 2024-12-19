from aiogram import types, F
from aiogram.types import ContentType
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import HELP_COMMAND

from KeyboardsBot import *


from aiogram import Router, types, F
# Бот# Роутер
router = Router()


from payments import *
from buymodul import PRICE

from moduls import os, load_dotenv

class Reg(StatesGroup):
    name = State()
    number = State()
    
# Хэндлер на команду /start
@router.message(Command("reg"))
async def cmd_start(message: types.Message,  state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите имя")
    
@router.message(Reg.name)
async def name_reg(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Введите номер телефона")

@router.message(Reg.number)
async def name_reg(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f"Регистрация завершена\nИмя: {data["name"]}\nНомер: {data["number"]}")
    await state.clear()



from mainfiles.requests import set_user


# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await set_user(message.from_user.id)
    await message.answer("Добро пожаловать! "
        "Данный бот еще находится на стадии разработки. Но он будет связан с покукой подписки Yandex+\n"
        f"{HELP_COMMAND}", reply_markup=ikb)
        
# Хэндлер на команду /help
@router.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer("Этот бот пока что в разработке.", reply_markup=ikb)

# Хэндлер на команду /buy
@router.message(Command('buy'))
async def buy(message: types.Message):
    load_dotenv()
    if os.getenv("PAYMENTS_TOKEN").split(':')[1] == 'TEST':
        await message.answer("Тестовый платеж!")
    await message.answer_invoice(title="Подписка на бота",
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