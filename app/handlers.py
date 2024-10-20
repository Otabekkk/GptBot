from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, F, Router

import app.keyboards as kb


router = Router()


# КОМАНДЫ
# ---------------------------------------------------- #
# Start
@router.message(CommandStart())
async def cmdStart(message: Message) -> None:
   await message.reply('Привет', reply_markup = kb.main)


# Help
@router.message(Command('help'))
async def get_help(message: Message) -> None:
    await message.answer('Пройдите к разработчику:', reply_markup = kb.toSanch)


# Sanjar
@router.message(F.text.lower() == 'санжар')
async def answerToQuestion(message: Message) -> None:
    await message.answer('Он мой разраб!')


# Getting Photo
@router.message(F.photo)
async def getPhoto(message: Message) -> None:
    await message.answer(f'Photo"s ID: {message.photo}')

# Sending photo
@router.message(Command('get_photo'))
async def getPhoto(message: Message) -> None:
    await message.answer_photo(photo = 'AgACAgIAAxkBAAMgZxPA_S0X0SE6UmBc0JOK91CzTb0AAoThMRs6kKFInvgVn0EvErYBAAMCAAN5AAM2BA', caption = 'Это от Санжара')
# ---------------------------------------------------- #