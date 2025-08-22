from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню (reply-кнопки)
def get_main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📂 Категории")],
            [KeyboardButton(text="📆 Меню на 1/7 дней")],
            [KeyboardButton(text="🔥 По калориям"), KeyboardButton(text="⏱ По времени")],
            [KeyboardButton(text="🧂 По ингредиентам")],
            [KeyboardButton(text="❓ FAQ"), KeyboardButton(text="📬 Связаться")]
        ],
        resize_keyboard=True
    )

# Подменю: Назад
back_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🔙 Назад")]],
    resize_keyboard=True
)

# Подменю: Выбор дней
choose_days_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1 день")],
        [KeyboardButton(text="7 дней")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

# Подменю: Выбор калорий
choose_calories_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1500"), KeyboardButton(text="2000")],
        [KeyboardButton(text="2500"), KeyboardButton(text="Свой вариант")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

# Подменю: Время (в минутах)
choose_time_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="10"), KeyboardButton(text="15")],
        [KeyboardButton(text="20"), KeyboardButton(text="30")],
        [KeyboardButton(text="Свой вариант")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

# Подменю: FAQ
faq_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Как работает бот?")],
        [KeyboardButton(text="Как сохранить рецепт?")],
        [KeyboardButton(text="Можно ли задать вопрос?")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)
