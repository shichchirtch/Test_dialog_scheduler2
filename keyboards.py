from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


pre_start_button = KeyboardButton(text='/start')

pre_start_clava = ReplyKeyboardMarkup(
    keyboard=[[pre_start_button]],
    resize_keyboard=True,
    input_field_placeholder='Приятного чтения'
)

sched_button = InlineKeyboardButton(text='▶️', callback_data='Zapusk' )

sched_kb = InlineKeyboardMarkup(
            inline_keyboard=[[sched_button]])