import config
import logging
# import Cats
# import Itmo
import markups as nav

from aiogram import Bot, Dispatcher, executor, types


# Вселенная
class World:
    def get_dict(self):
        return dict([('😂', "01"), ('🥵', "02"), ('😡', "03"), ('😰', "04"), ('🥺', "05")])


# котики
class Cats:
    def get_dict(self):
        return dict([('😂', 'aiogram_pictures/cat_1.jpg'), ('🥵', 'aiogram_pictures/cat_2.jpg'), ('😡', 'aiogram_pictures/cat_3.jpg'), ('😰', 'aiogram_pictures/cat_4.jpg'), ('🥺', 'aiogram_pictures/cat_5.jpg')])

#ITMO
class Itmo:
    def get_dict(self):
        return dict([('😂', 21), ('🥵', 22), ('😡', 23), ('😰', 24), ('🥺', 25)])


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
            await message.answer("Отлично! Осталось за малым, выбирай смайлик", reply_markup=nav.emojiMenu)
            x = 1
        elif "итмо" in message.text.lower():
            world = Itmo()
            await message.answer("Отлично! Осталось за малым, выбирай смайлик", reply_markup=nav.emojiMenu)
            x = 1
        else:
            await message.answer("Мне кажется, лучше следовать инструкции и выбирать вселенную из предложенных в менюшке 😉", reply_markup=nav.worldMenu)
        return

    if x == 1:
        if '😂' in message.text:
            media = types.MediaGroup()
            media.attach_photo(types.InputFile(world.get_dict()['😂']))
            await message.answer_media_group(media=media)
        elif '🥵' in message.text:
            media = types.MediaGroup()
            media.attach_photo(types.InputFile(world.get_dict()['🥵']))
            await message.answer_media_group(media=media)
        elif '😡' in message.text:
            media = types.MediaGroup()
            media.attach_photo(types.InputFile(world.get_dict()['😡']))
            await message.answer_media_group(media=media)
        elif '😰' in message.text:
            media = types.MediaGroup()
            media.attach_photo(types.InputFile(world.get_dict()['😰']))
            await message.answer_media_group(media=media)
        elif '🥺' in message.text:
            media = types.MediaGroup()
            media.attach_photo(types.InputFile(world.get_dict()['🥺']))
            await message.answer_media_group(media=media)
        elif "Выбрать вселенную" in message.text:
            await message.answer("Правильно, выбери что-нибудь ещё", reply_markup=nav.worldMenu)
            x = 0
        else:
            await message.answer("Извини, похоже у меня ничего нет с этим смайликом 😔. Попробуй снова, но присылай через меню", reply_markup=nav.emojiMenu)




# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
