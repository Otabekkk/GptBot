from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Контакты 👥'), KeyboardButton(text = 'О проекте 🏷️')],
    [KeyboardButton(text = 'Начать 🔭'), KeyboardButton(text = 'Список команд 📜')]
], resize_keyboard = True, input_field_placeholder = 'Выберите пункт...')

toSanch = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Разработчик', url = 'https://t.me/ch1kzz')]
])

mainAutor = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Даниил', url = 'https://t.me/ch1kzz')]
])

# afterStart = ReplyKeyboardMarkup(keyboard = [
#     [KeyboardButton(text = 'Отправить информацию о товаре')]
# ], resize_keyboard = True)

returnKeyboard = ReplyKeyboardRemove()