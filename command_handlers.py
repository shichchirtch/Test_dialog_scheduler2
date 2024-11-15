from aiogram import Router
import asyncio
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from bot_base import user_dict, users_db
from filters import PRE_START, IS_ADMIN
from lexicon import *
from copy import deepcopy
from aiogram.fsm.context import FSMContext
from keyboards import pre_start_clava
from bot_instans import FSM_ST, ADMIN
from aiogram_dialog import DialogManager, StartMode


ch_router = Router()


@ch_router.message(CommandStart(), PRE_START())
async def command_start_process(message:Message, dialog_manager: DialogManager, state:FSMContext):
    users_db[message.from_user.id] = deepcopy(user_dict)
    await state.set_data({'foto_id':'', 'lan':'ru'})
    await message.answer(text=f'👋\n\n<b>Привет, {message.from_user.first_name}!</b>\n'
           'Это планировщик бот. скажи мне когда произойдёт важное для тебя событие'
                              ' и я напомню тебе о нем забалаговременно !\n\nУдобно, не правда ли ?', reply_markup=ReplyKeyboardRemove())
    await dialog_manager.start(state=FSM_ST.start, mode=StartMode.RESET_STACK)




@ch_router.message(PRE_START())
async def before_start(message: Message):
    prestart_ant = await message.answer(text='Klicken auf <b>start</b> !',
                                        reply_markup=pre_start_clava)
    await message.delete()
    await asyncio.sleep(3)
    await prestart_ant.delete()

@ch_router.message(Command('admin'), IS_ADMIN())
async def basic_menu_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(ADMIN.first)
    await asyncio.sleep(1)
    await message.delete()


@ch_router.message(Command('basic_menu'))
async def basic_menu_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=FSM_ST.vor_mahnung, mode=StartMode.RESET_STACK)


@ch_router.message(Command('help'))
async def basic_menu_start(message: Message, dialog_manager: DialogManager):
    await message.answer(text=help_text)
    await dialog_manager.start(state=FSM_ST.vor_mahnung, mode=StartMode.RESET_STACK)



