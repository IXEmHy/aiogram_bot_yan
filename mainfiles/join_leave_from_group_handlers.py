# from aiogram.utils.chat_member import ADMINS
# проверка на наличие прав у бота
# isinstance(await bot.get_chat_member(message.chat.id, bot.id), ADMINS)
    #await bot.delete_message(message.chat.id, message.message_id)
# from aiogram.types import ChatMemberUpdated
# from aiogram.filters import ChatMemberUpdatedFilter
# from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER
# Проверка на вступление выход из группы (только если бот является админом)
# @router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
# async def on_user_leave(event: ChatMemberUpdated): 
#     await event.answer('Печально')
#     with open("print.txt", "w") as f:
#          f.write(f"Member {event.from_user.full_name} with {event.from_user.id} was leaved")

# @router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
# async def on_user_join(event: ChatMemberUpdated): 
#     with open("print.txt", "w") as f:
#         f.write(f"Member {event.from_user.full_name} with {event.from_user.id} was joined")