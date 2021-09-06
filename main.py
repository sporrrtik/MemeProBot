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
        return dict([('😂', 11), ('🥵', 12), ('😡', 13), ('😰', 14), ('🥺', 15)])

#ITMO
class Itmo:
    def get_dict(self):
        return dict([('😂', 21), ('🥵', 22), ('😡', 23), ('😰', 24), ('🥺', 25)])


# log level
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
world = World()

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
    if "😸 Котики" in message.text:
        world = Cats()
        await message.answer("Отлично! Осталось за малым, выбирай смайлик", reply_markup=nav.emojiMenu)
    elif "👨‍💻 Итмо" in message.text:
        world = Itmo()
        await message.answer("Отлично! Осталось за малым, выбирай смайлик", reply_markup=nav.emojiMenu)
    # else:
    #     world.get_dict()
    #     await message.answer("Хммм", reply_markup=nav.emojiMenu)

#await message.answer(world.get_dict()['😂'] + "\nПонравилось?)\nЕсли надо ещё, продолжай отправлять смайлики!")

    elif '😂' in message.text:
        await message.answer(world.get_dict()['😂'])
    elif '🥵' in message.text:
        await message.answer(world.get_dict()['🥵'])
    elif '😡' in message.text:
        await message.answer(world.get_dict()['😡'])
    elif '😰' in message.text:
        await message.answer(world.get_dict()['😰'])
    elif '🥺' in message.text:
        await message.answer(world.get_dict()['🥺'])
    elif "Выбрать вселенную" in message.text:
        await message.answer("Правильно, выбери что-нибудь ещё", reply_markup=nav.worldMenu)
    else:
        await message.answer("Извини, похоже у меня ничего нет с этим смайликом или ты просто сделал что-то не так 😔. Попробуй снова", reply_markup=nav.worldMenu)



# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
