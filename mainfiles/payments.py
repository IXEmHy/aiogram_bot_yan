from aiogram.types import ContentType
from aiogram import types, F

from comands_handlers import router

# Обработчик платежей
# # pre checkout  (must be answered in 10 seconds)
# @router.pre_checkout_query(lambda query: True)
# async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# # successful payment
# @router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
# async def successful_payment(message: types.Message):
#     print("SUCCESSFUL PAYMENT:")
#     payment_info = message.successful_payment
#     for k, v in payment_info:
#         print(f"{k} = {v}")

#     await bot.send_message(message.chat.id,
#                            f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!")

