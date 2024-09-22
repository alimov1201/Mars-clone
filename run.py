from aiogram import Bot, Dispatcher, F
import asyncio
from app.config import TOKEN
from app.handlers import router
from app.handlers import student

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    
    except KeyboardInterrupt:
        print('')
        
    finally:
        student.clear()