import asyncio
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, ManagedMultiselect, ManagedRadio
from aiogram_dialog.api.entities.modes import ShowMode, StartMode
from bot_instans import dp, bot_storage_key
from bot_base import users_db
import pickle
from datetime import date
from bot_instans import FSM_ST, MAHNUNG
from keyboards import sched_kb
from scheduler_functions import scheduler_job


async def on_date_selected(callback: CallbackQuery, widget,
                           manager: DialogManager, selected_date: date):
    await callback.message.answer(f"Вы выбрали дату: {selected_date}")
    print('callback.data = ', callback.data)  # 8CvuU6calendar:173274840
    await manager.next()
    manager.show_mode = ShowMode.SEND


async def button_uhr_clicked(callback: CallbackQuery, widget: Button,
                             manager: DialogManager):
    print('calender_callback = ', callback.data)  #
    # await asyncio.sleep(0.5)
    await callback.message.answer(callback.data)
    await manager.next()
    manager.show_mode = ShowMode.SEND


async def button_min_clicked(callback: CallbackQuery, widget: Button,
                             manager: DialogManager):
    print('calender_callback = ', callback.data)  #
    # await asyncio.sleep(0.5)
    await callback.message.answer(callback.data)

    # await manager.done()# start(MAHNUNG.mahnung_start)


async def button_zapusk_clicked(callback: CallbackQuery, widget: Button,
                             manager: DialogManager):
    # await callback.message.answer('Жми', reply_markup=sched_kb)
    await manager.next()




# async def button_zapusk_clicked(callback: CallbackQuery, widget: Button,
#                              manager: DialogManager):
#     await callback.message.answer('Жми', reply_markup=sched_kb)
#     bg_manager = manager.bg(
#         user_id=callback.from_user.id,
#         chat_id=callback.message.chat.id,
#         stack_id=manager.current_stack().id
#     )
#     state = manager.middleware_data["state"]
#     us_dict = await state.get_data()
#     bg_manager = manager.bg(
#         user_id=callback.from_user.id,
#         chat_id=callback.message.chat.id,
#         stack_id=manager.current_stack().id
#     )
#     us_dict['bg_man'] = bg_manager
#     await state.set_data(us_dict)
#     await bg_manager.done()



