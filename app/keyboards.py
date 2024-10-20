from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup ,InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Инструкции 📜'), KeyboardButton(text = 'О  нас 🔗')],
    [KeyboardButton(text = 'Контакты 👥'), KeyboardButton(text = 'О проекте 🏷️')],
    [KeyboardButton(text = 'Начать 🔭')]
], resize_keyboard = True, input_field_placeholder = 'Выберите пункт...')

toSanch = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Разработчик', url = 'https://t.me/ch1kzz')]
])