from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup
from config import HELP_COMMAND
commands = HELP_COMMAND.split(":")[1].split('\n')[1:]

StartsCommands = [KeyboardButton(text=x) for x in commands]

KeyboardButtonArgs = [
    StartsCommands,
]

kb = ReplyKeyboardMarkup(
  keyboard = KeyboardButtonArgs,
  one_time_keyboard=True
)


ikb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=x, callback_data=x[1:]) for x in commands]])
