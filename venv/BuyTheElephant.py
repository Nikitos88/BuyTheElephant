# my second program. buy the elephant
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

PROXY_URL = "http://proxy.server:3128"
bot = Bot(token=os.environ.get('TOKEN'), proxy=PROXY_URL)
dp = Dispatcher(bot)

#echo
@dp.message_handler()
async def echo(message: types.Message):
    if message: types.Message
    #await message.answer(message.text)
    await message.answer('Все говорят:  ' + '"' + message.text + '"' + ', а ты купи слона.')

    # run long-polling
if __name__== "__main__":
    executor.start_polling(dp, skip_updates=True)