from aiogram.fsm.state import State, StatesGroup

class MenuState(StatesGroup):
    choosing_calories = State()
    choosing_time = State()
    entering_ingredients = State()

class FullMenuState(StatesGroup):
    choosing_days = State()
    choosing_kcal = State()
    entering_custom_kcal = State()
    entering_excluded = State()
    entering_preferred = State()
