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
async def sendPhoto(message: Message) -> None:
    await message.answer_photo(photo = 'AgACAgIAAxkBAAMgZxPA_S0X0SE6UmBc0JOK91CzTb0AAoThMRs6kKFInvgVn0EvErYBAAMCAAN5AAM2BA', caption = 'Это от Санжара')

# Список команд
@router.message(F.text == 'Список команд 📜')
async def instructions(message: Message) -> None:
    await message.answer('Вот список команд, которые вы можете использовать:\n/start - запуск бота\n/help - получить помощь')

# Контакты
@router.message(F.text == 'Контакты 👥')
async def contacts(messaage: Message) -> None:
    await messaage.answer('Автор идеи и владелец бота:', reply_markup = kb.mainAutor)

# О проекте
@router.message(F.text == 'О проекте 🏷️')
async def aboutProject(message: Message) -> None:
    await message.answer('Это коммерческий проект\n\nИдея проекта заключается в том, чтобы содать бота, который автоматизирует обработку запросов пользователей')

# Start
@router.message(F.text == 'Начать 🔭')
async def start(message: Message) -> None:
    await message.answer('Ну чтож, давайте приступим, строго следуйте инструкции', reply_markup = kb.returnKeyboard)

    await message.answer('1: Отправьте мне название товара')
    with open('user.txt', 'a', encoding='UTF-8') as file:
        file.write(f"Название товара: {message.text}\n")

    await message.answer('2: отправьте мне описание товара')
    with open('user.txt', 'a', encoding='UTF-8') as file:
        file.write(f"Описание товара: {message.text}\n")

    await message.answer('3: Отправьте мне фото товара')
    if message.photo:
        photo_id = message.photo[-1].file_id  # Получаем ID самого большого размера фотографии
        with open('user.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Фото товара: {photo_id}\n")
# ---------------------------------------------------- #