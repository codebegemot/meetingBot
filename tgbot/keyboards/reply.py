from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hello_kb = ReplyKeyboardMarkup()
hello_btn = KeyboardButton("Hello!")
hello_kb.add(hello_btn)