from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup()
hello_btn = InlineKeyboardButton("Hello!")
start_keyboard.add(hello_btn)
