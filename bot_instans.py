from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import StorageKey, MemoryStorage
from aiogram.fsm.state import State, StatesGroup

from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

aio_storage = MemoryStorage()


class FSM_ST(StatesGroup):
    start = State()  # FSM_ST:start
    uhr = State()
    minuten = State()
    vor_mahnung = State()
    nach_mahnung_accepting = State()

class MAHNUNG(StatesGroup):
    mahnung_start = State()
    mahnung_gearbeitet = State()
    nach_mahnung = State()


class VAC(StatesGroup):
    empty = State()
    full = State()

class ADMIN(StatesGroup):
    first = State()



BOT_TOKEN = 'BOT TOKEN'

bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

bot_storage_key = StorageKey(bot_id=bot.id, user_id=bot.id, chat_id=bot.id)

dp = Dispatcher(storage=aio_storage)

