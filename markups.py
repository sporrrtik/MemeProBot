from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("Выбрать вселенную")

# --- Меню вселенных ---
btnItmo = KeyboardButton("👨‍💻 Итмо‍")
btnCats = KeyboardButton("😸 Котики")
btnOld = KeyboardButton(" Old_But_Gold")
btnFun = KeyboardButton("Грущу, просто развеселите 😔")
worldMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCats, btnItmo, btnOld, btnFun)

# --- Меню смайлов котиков ---
btnCatEmoji1 = KeyboardButton("😂")
btnCatEmoji2 = KeyboardButton("🥵")
btnCatEmoji3 = KeyboardButton("😡")
btnCatEmoji4 = KeyboardButton("😰")
btnCatEmoji5 = KeyboardButton("🥺")
CatEmojiMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCatEmoji5, btnCatEmoji4, btnCatEmoji3,
                                                             btnCatEmoji2, btnCatEmoji1, btnMain)

# --- Меню смайлов олдов ---
btnOldEmoji1 = KeyboardButton('🖕')
btnOldEmoji2 = KeyboardButton('👍')
btnOldEmoji3 = KeyboardButton('😔')
btnOldEmoji4 = KeyboardButton('🤨')
btnOldEmoji5 = KeyboardButton('😋')
btnOldEmoji6 = KeyboardButton('🤪')
btnOldEmoji7 = KeyboardButton('😂')
btnOldEmoji8 = KeyboardButton('😡')
OldEmojiMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOldEmoji8, btnOldEmoji7, btnOldEmoji6, btnOldEmoji5, btnOldEmoji4,
                                                             btnOldEmoji3, btnOldEmoji2, btnOldEmoji1, btnMain)
