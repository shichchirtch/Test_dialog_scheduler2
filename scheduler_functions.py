from random import shuffle, sample
from aiogram.types import CallbackQuery
from datetime import datetime, timedelta
from bot_instans import bot, scheduler, FSM_ST, MAHNUNG
from aiogram.fsm.context import FSMContext
from lexicon import *
from bot_base import users_db
from aiogram_dialog import DialogManager
# from aiogram_dialog.manager import BackgroundDialogManager
# from aiogram_dialog.api.bg_manager import BackgroundDialogManager


async def mahnung_gearbeitet(bot, user_id):
    print('WE are into mahnung gearbeitet function')
    # print('nach bg_manager   ---> ', bg_manager)  # nach bg_manager   --->  <aiogram_dialog.manager.bg_manager.BgManager object at 0x0000026798EFCF10>
    await bot.send_message(chat_id=user_id, text="Mahnung !")


def scheduler_job(callback: CallbackQuery, widget, manager):# bg_manager):
    user_id = callback.from_user.id
    print(f'scheduler_job works for user {user_id}')
    time_now = datetime.now()  # Время сейчас
    print('time_now = ', time_now)
    delta = timedelta(seconds=10)  # Время, Через которое придёт сообщуха
    future = time_now+delta  # Время когда действие должно быть закончено
    stop_exam = 'exam'+str(user_id)
    print('8888888')
    scheduler.add_job(mahnung_gearbeitet, "date", run_date=future, args=(bot, user_id), id=stop_exam)


# def scheduler_job(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     print(f'scheduler_job works for user {user_id}')
#     time_now = datetime.now()
#     future = time_now + timedelta(seconds=10)
#     stop_exam = 'exam' + str(user_id)
#
#     scheduler.add_job(mahnung_gearbeitet, "date", run_date=future, args=(bot, user_id), id=stop_exam)