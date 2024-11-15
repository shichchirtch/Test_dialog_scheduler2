from aiogram import Router
from filters import ZAPUSK_FILTER
from aiogram.filters import StateFilter
from contextlib import suppress
from aiogram.types import CallbackQuery, InputMediaPhoto
from bot_base import users_db
from aiogram.exceptions import TelegramBadRequest
from lexicon import *
from aiogram.fsm.context import FSMContext
from bot_instans import FSM_ST, dp, bot_storage_key
from keyboards import sched_kb
from random import choice
from scheduler_functions import scheduler_job
from aiogram_dialog import DialogManager

cb_router = Router()

@cb_router.callback_query(ZAPUSK_FILTER())
async def zapusk_cb_process(callback: CallbackQuery, state: FSMContext):
    print('zapusk_process works')
    us_dict = await state.get_data()
    bg_manager = us_dict.get('bg_man')
    if bg_manager:
        await scheduler_job(callback, bg_manager)
    else:
        print("Ошибка: bg_manager не найден в state")

    # await scheduler_job(callback, bg_manager)
