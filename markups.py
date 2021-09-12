from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("Выбрать вселенную")

# --- Меню вселенных ---
btnItmo = KeyboardButton("👨‍💻 Итмо‍")
btnCats = KeyboardButton("😸 Котики")
worldMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCats, btnItmo)

# --- Меню смайлов ---
btnEmoji1 = KeyboardButton("😂")
btnEmoji2 = KeyboardButton("🥵")
btnEmoji3 = KeyboardButton("😡")
btnEmoji4 = KeyboardButton("😰")
btnEmoji5 = KeyboardButton("🥺")
emojiMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEmoji5, btnEmoji4, btnEmoji3, btnEmoji2, btnEmoji1, btnMain)