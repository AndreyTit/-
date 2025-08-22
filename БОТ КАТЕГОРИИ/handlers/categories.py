from aiogram import Router, F
from aiogram.types import (
    Message, KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
)
import json

from config import RECIPES_PATH

router = Router()

# Загружаем рецепты
def load_recipes():
    with open(RECIPES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Получаем все уникальные категории
def get_categories():
    data = load_recipes()
    return sorted(set(d['category'] for d in data))

# 📂 Кнопка "Категории" → reply-кнопки категорий
@router.message(F.text == "📂 Категории")
async def show_categories(message: Message):
    categories = get_categories()
    kb = [[KeyboardButton(text=cat)] for cat in categories]
    kb.append([KeyboardButton(text="🏠 Главное меню")])
    await message.answer("Выберите категорию 🍽", reply_markup=ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True))

# Показываем блюда категории (первые 5) через inline-кнопки
@router.message(lambda msg: msg.text in get_categories())
async def show_category_dishes(message: Message):
    category = message.text
    data = load_recipes()
    dishes = [d for d in data if d['category'] == category]
    limited = dishes[:5]

    buttons = [
        [InlineKeyboardButton(text=d["title"], callback_data=f"dish_{d['title']}")]
        for d in limited
    ]
    if len(dishes) > 5:
        buttons.append([InlineKeyboardButton(text="➡️ Далее", callback_data=f"more_{category}_5")])

    await message.answer(
        f"🥗 Блюда из категории: <b>{category}</b>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons),
        parse_mode="HTML"
    )

# Обработка кнопки "Далее" — следующая порция блюд
@router.callback_query(F.data.startswith("more_"))
async def show_more_dishes(callback: CallbackQuery):
    parts = callback.data.split("_")
    category = parts[1]
    offset = int(parts[2])

    data = load_recipes()
    dishes = [d for d in data if d['category'] == category]
    next_dishes = dishes[offset:offset+5]

    buttons = [
        [InlineKeyboardButton(text=d["title"], callback_data=f"dish_{d['title']}")]
        for d in next_dishes
    ]

    new_offset = offset + 5
    if new_offset < len(dishes):
        buttons.append([InlineKeyboardButton(text="➡️ Далее", callback_data=f"more_{category}_{new_offset}")])
    else:
        buttons.append([InlineKeyboardButton(text="🔄 Сначала", callback_data=f"more_{category}_0")])

    await callback.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )
    await callback.answer()

# Обработка нажатия на блюдо → показать карточку
@router.callback_query(F.data.startswith("dish_"))
async def show_dish_card(callback: CallbackQuery):
    dish_title = callback.data[5:]
    data = load_recipes()
    dish = next((d for d in data if d["title"] == dish_title), None)

    if not dish:
        await callback.answer("Блюдо не найдено 😔", show_alert=True)
        return

    text = (
        f"🍽 <b>{dish['title']}</b>\n\n"
        f"🏷 Категория: {dish['category']}\n"
        f"🔗 <a href='{dish['link']}'>Перейти к рецепту</a>"
    )

    await callback.message.answer(text, parse_mode="HTML", disable_web_page_preview=True)
    await callback.answer()

# Регистрируем обработчик
def register_category_handlers(dp):
    dp.include_router(router)
