from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext

router = Router()

# Функция главного меню (без кнопки "Главное меню")
def get_main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📂 Категории")],
            [KeyboardButton(text="❓ FAQ"), KeyboardButton(text="📬 Связаться")]
        ],
        resize_keyboard=True
    )

@router.message(F.text == "/start")
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()  # Очищаем состояние при старте
    await message.answer(
        "👋 Привет!",
        reply_markup=get_main_menu()
    )

@router.message(F.text == "🏠 Главное меню")
async def back_to_main(message: Message, state: FSMContext):
    await state.clear()  # Очищаем состояние при возврате в главное меню
    await message.answer("🔙 Главное меню", reply_markup=get_main_menu())
