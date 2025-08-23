from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda msg: msg.text == "📬 Связаться")
async def contact_author(message: Message):
    await message.answer(
        "📬 <b>По вопросам сотрудничества, рекламы и предложений</b>\n\n"
        "Пиши напрямую: @KindlA",  # ← замени на свой username
        parse_mode="HTML"
    )

def register_contact_handlers(dp):
    dp.include_router(router)
