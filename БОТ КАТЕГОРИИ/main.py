import asyncio
from config import TOKEN, RECIPES_PATH
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand  # ✅ импортируем команды
from handlers import register_all_handlers

# Создаём бота
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

register_all_handlers(dp)

# ✅ Функция для меню команд
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота"),
    ]
    await bot.set_my_commands(commands)

async def main():
    try:
        print("🔄 Запуск бота...")
        # Устанавливаем команды при запуске
        await set_commands(bot)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Ошибка при запуске: {e}")

if __name__ == "__main__":
    asyncio.run(main())
