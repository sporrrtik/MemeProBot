import config
import logging
# import Cats
# import Itmo
import markups as nav

from aiogram import Bot, Dispatcher, executor, types


# --- Вселенная ---
class World:
    def get_dict(self):
        return dict([('😂', "01"), ('🥵', "02"), ('😡', "03"), ('😰', "04"), ('🥺', "05")])


# --- Котики ---
class Cats:
    def get_dict(self):
        return dict([('😂', 'aiogram_pictures/cat_1.jpg'), ('🥵', 'aiogram_pictures/cat_2.jpg'), ('😡', 'aiogram_pictures/cat_3.jpg'), ('😰', 'aiogram_pictures/cat_4.jpg'), ('🥺', 'aiogram_pictures/cat_5.jpg')])

# --- ITMO ---
class Itmo:
    def get_dict(self):
        return dict([('😂', 21), ('🥵', 22), ('😡', 23), ('😰', 24), ('🥺', 25)])

# --- Old But Gold ---
class OLdButGold:
    def get_dict(self):
        return dict([('😂', 'aiogram_pictures/old_1.jpg'),('🤪', 'aiogram_pictures/old_2.jpg'), ('😡', 'aiogram_pictures/old_3.jpg'),
                     ('😋', 'aiogram_pictures/old_4.jpg'), ('🤨', 'aiogram_pictures/old_5.jpg'), ('😔', 'aiogram_pictures/old_6.jpg'),
                     ('👍', 'aiogram_pictures/old_7.jpg'), ('🖕', 'aiogram_pictures/old_8.jpg')])


# log level
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
world = World()
x = 0

# voice delete
#   @dp.message_handler(content_types=[""])

# welcome
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Ой, ты похоже новенький... Ну присаживайся, для тебя всегда место найдётся." + '😉\n' + "В общем я бот, который поменяет " +
        "твои смайлики на что-то более интересное " + '😚\n' + "Просто выбери интересующую тебя тему, а затем смайлик", reply_markup= nav.worldMenu)


# echo
@dp.message_handler()
async def echo(message: types.Message):
    global world
    global x

    if x == 0:
        if "кот" in message.text.lower():
            world = Cats()
            await message.answer("Отлично! Осталось за малым, выбирай смайлик", reply_markup=nav.CatEmojiMenu)
            x = 1
        elif "итмо" in message.text.lower():
            world = Itmo()
            await message.answer("Выбрал итмо и теперь хочешь выбрать смайлик? Ха-ха, наивный\nВыбирай итмо и не выбирай вообще! Поэтому выбирай другие вселенные", reply_markup=nav.worldMenu)
            media = types.MediaGroup()
            media.attach_photo(types.InputFile('aiogram_pictures/itmo.jpg'))
            await message.answer_media_group(media=media)
        elif "old" in message.text.lower():
            world = OLdButGold()
            await message.answer("Хороший выбор! А теперь смайлик", reply_markup=nav.OldEmojiMenu)
            x = 1
        elif "😔" in message.text:
            await message.answer("Не переживай, развеселим😉. Но пока что рубрика в доработке", reply_markup=nav.worldMenu)
            # x = 3
        else:
            await message.answer("Мне кажется, лучше следовать инструкции и выбирать вселенную из предложенных в менюшке 😉", reply_markup=nav.worldMenu)
        return

    if x == 1:
        # if '😂' in message.text:
        #     media = types.MediaGroup()
        #     media.attach_photo(types.InputFile(world.get_dict()['😂']))
        #     await message.answer_media_group(media=media)
        # elif '🥵' in message.text:
        #     media = types.MediaGroup()
        #     media.attach_photo(types.InputFile(world.get_dict()['🥵']))
        #     await message.answer_media_group(media=media)
        # elif '😡' in message.text:
        #     media = types.MediaGroup()
        #     media.attach_photo(types.InputFile(world.get_dict()['😡']))
        #     await message.answer_media_group(media=media)
        # elif '😰' in message.text:
        #     media = types.MediaGroup()
        #     media.attach_photo(types.InputFile(world.get_dict()['😰']))
        #     await message.answer_media_group(media=media)
        # elif '🥺' in message.text:
        #     media = types.MediaGroup()
        #     media.attach_photo(types.InputFile(world.get_dict()['🥺']))
        #     await message.answer_media_group(media=media)
        # elif "Выбрать вселенную" in message.text:
        #     await message.answer("Правильно, выбери что-нибудь ещё", reply_markup=nav.worldMenu)
        #     x = 0
        if message.text in ['😂', '🥵', '😰', '😡', '🥺', '🤪', '😋', '🤨','😔', '👍', '🖕']:
            media = types.MediaGroup()
            media.attach_photo(types.InputFile(world.get_dict()[message.text]))
            await message.answer_media_group(media=media)
        elif "Выбрать вселенную" in message.text:
            await message.answer("Правильно, выбери что-нибудь ещё", reply_markup=nav.worldMenu)
            x = 0
        else:
            await message.answer("Извини, похоже у меня ничего нет с этим смайликом 😔. Попробуй снова, но присылай через меню", reply_markup=nav.CatEmojiMenu)
    # elif x == 2:
    #     if message.text in ['🤪', '😋', '🤨','😔', '👍', '🖕', '😂', '😰']:
    #




# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
