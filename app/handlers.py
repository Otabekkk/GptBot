from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, F, Router

import app.keyboards as kb


router = Router()

userStates = {}

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
    await message.answer('Это коммерческий проект\n\nИдея проекта заключается в том, чтобы создать бота, который автоматизирует обработку запросов пользователей')


# Start
@router.message(F.text == 'Начать 🔭')
async def start(message: Message) -> None:
    userId = message.from_user.id

    await message.answer('Ну чтож, давайте приступим, строго следуйте инструкции', reply_markup = kb.returnKeyboard)
    
    userStates[message.from_user.id] = 'waiting'

    await message.answer('1: Отправьте мне название товара')
    
@router.message(F.text)
async def getproductName(message: Message) -> None:
    userId = message.from_user.id

    if userStates.get(userId) == 'waiting':
        with open('user.txt', 'a', encoding='UTF-8') as file:
            file.write(f"ID: {userId} Название товара: {message.text}\n")
        
        await message.reply("Название сохранено.")
        userStates[userId] = 'waiting_for_description'
        await message.answer('2: отправьте мне описание товара')

    elif userStates.get(userId) == 'waiting_for_description':

        with open('user.txt', 'a', encoding='UTF-8') as file:
            file.write(f"ID: {userId} Описание товара: {message.text}\n")


        await message.reply("Описание сохранено. Спасибо!")
        # Сбрасываем состояние пользователя
        userStates.pop(userId, None)
    
    else:
        await message.reply("Я вас не понял. Попробуйте еще раз.")

    # await message.answer('3: Отправьте мне фото товара')
    # if message.photo:
    #     photo_id = message.photo[-1].file_id  # Получаем ID самого большого размера фотографии
    #     with open('user.txt', 'a', encoding='UTF-8') as file:
    #         file.write(f"Фото товара: {photo_id}\n")
# ---------------------------------------------------- #



# from aiogram import Bot, Dispatcher, types, F, Router
# from aiogram.types import Message
# from aiogram.filters import CommandStart, Command
# import app.keyboards as kb

# router = Router()

# # Храним состояния пользователя
# userStates = {}

# # КОМАНДЫ
# # ---------------------------------------------------- #
# # Start
# @router.message(CommandStart())
# async def cmdStart(message: Message) -> None:
#     await message.reply('Привет', reply_markup=kb.main)


# # Start the process with the "Начать" button
# @router.message(F.text == 'Начать 🔭')
# async def start(message: Message) -> None:
#     user_id = message.from_user.id
#     userStates[user_id] = 'waiting_for_product_name'
    
#     await message.answer('Ну что ж, давайте приступим. 1: Отправьте мне название товара', reply_markup=kb.returnKeyboard)


# # Обработка получения названия товара
# @router.message(F.text)
# async def get_product_name(message: Message) -> None:
#     user_id = message.from_user.id
    
#     if userStates.get(user_id) == 'waiting_for_product_name':
#         product_name = message.text

#         # Записываем название товара в файл
#         with open('user.txt', 'a', encoding='utf-8') as file:
#             file.write(f"Название товара: {product_name}\n")
        
#         await message.reply("Название сохранено. Теперь введите описание товара:")
#         userStates[user_id] = 'waiting_for_product_description'
    
#     elif userStates.get(user_id) == 'waiting_for_product_description':
#         product_description = message.text

#         # Записываем описание товара в файл
#         with open('user.txt', 'a', encoding='utf-8') as file:
#             file.write(f"Описание товара: {product_description}\n\n")
        
#         await message.reply("Описание сохранено. Спасибо!")
#         # Сбрасываем состояние пользователя
#         userStates.pop(user_id, None)
#     else:
#         await message.reply("Я вас не понял. Попробуйте еще раз.")
# # ---------------------------------------------------- #
