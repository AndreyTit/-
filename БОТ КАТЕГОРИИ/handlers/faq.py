from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda msg: msg.text == "❓ FAQ")
async def show_faq(message: Message):
    text = (
        "1️⃣ <b>Как работает бот?</b>\n"
        "Все рецепты разбиты на категории - выбирай категорию - нажимай на название блюда - бот покажет тебе рецепт в наших каналах.\n\n"
        
        "2️⃣ <b>Можно ли сохранять любимые рецепты?</b>\n"
        "Сейчас эта функция в разработке. Скоро появится возможность добавить рецепты в Избранное.\n\n"
        
        "3️⃣ <b>Как связаться с автором или задать вопрос?</b>\n"
        "Нажми кнопку «📬 Связаться» в главном меню.\n\n"

        "💡 Если остались вопросы — пиши нам! Мы всегда на связи."
    )
    await message.answer(text)

def register_faq_handlers(dp):
    dp.include_router(router)
