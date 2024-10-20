from config import TOKEN, API

import logging

import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router


bot = Bot(token = TOKEN)
dp = Dispatcher()



async def main() -> None:
   dp.include_router(router = router)
   await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')