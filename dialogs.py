from aiogram_dialog import Dialog, StartMode, Window
from getters import get_languages, get_spam, get_skills
from bot_instans import FSM_ST, MAHNUNG, VAC
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Row, Column, Multiselect, Group, Radio, Next, Start, Calendar
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram.types import ContentType
from callback_dialogs import (radio_button_clicked, category_filled,
                              radio_spam_button_clicked, on_confirm_clicked, go_to_next_dialog)
import operator
from lexicon import *
from dialog_functions import name_check, mail_check
from input_handlers import (correct_name_handler, error_name_handler,
                            error_mail_handler, correct_mail_handler, on_photo_sent,
                            message_not_foto_handler)
from calendar_functions import on_date_selected, button_uhr_clicked, button_min_clicked, button_zapusk_clicked
from scheduler_functions import scheduler_job

start_dialog = Dialog(
    Window(
        Const('Выберите ДАТУ 👇'),
        Calendar(id='calendar',
                 on_click=on_date_selected),
        state=FSM_ST.start,
    ),

    Window(
        Const('Выбирерите время  ( часы ) ?'),
        Row(
            Button(text=Const('00'), id='button_00', on_click=button_uhr_clicked),
            Button(text=Const('01'), id='button_1', on_click=button_uhr_clicked),
            Button(text=Const('02'), id='button_2', on_click=button_uhr_clicked),
            Button(text=Const('03'), id='button_3', on_click=button_uhr_clicked),
            Button(text=Const('04'), id='button_4', on_click=button_uhr_clicked),
            Button(text=Const('05'), id='button_5', on_click=button_uhr_clicked), ),
        Row(
            Button(text=Const('06'), id='button_6', on_click=button_uhr_clicked),
            Button(text=Const('07'), id='button_7', on_click=button_uhr_clicked),
            Button(text=Const('08'), id='button_8', on_click=button_uhr_clicked),
            Button(text=Const('09'), id='button_9', on_click=button_uhr_clicked),
            Button(text=Const('10'), id='button_10', on_click=button_uhr_clicked),
            Button(text=Const('11'), id='button_11', on_click=button_uhr_clicked), ),
        Row(
            Button(text=Const('12'), id='button_12', on_click=button_uhr_clicked),
            Button(text=Const('13'), id='button_13', on_click=button_uhr_clicked),
            Button(text=Const('14'), id='button_14', on_click=button_uhr_clicked),
            Button(text=Const('15'), id='button_15', on_click=button_uhr_clicked),
            Button(text=Const('16'), id='button_16', on_click=button_uhr_clicked),
            Button(text=Const('17'), id='button_17', on_click=button_uhr_clicked), ),
        Row(
            Button(text=Const('18'), id='button_18', on_click=button_uhr_clicked),
            Button(text=Const('19'), id='button_19', on_click=button_uhr_clicked),
            Button(text=Const('20'), id='button_20', on_click=button_uhr_clicked),
            Button(text=Const('21'), id='button_21', on_click=button_uhr_clicked),
            Button(text=Const('22'), id='button_22', on_click=button_uhr_clicked),
            Button(text=Const('23'), id='button_23', on_click=button_uhr_clicked)
        ),
        state=FSM_ST.uhr,
    ),

    Window(
        Const('Выбирите минуты'),
        Row(
            Button(text=Const('00'), id='button_00', on_click=button_min_clicked),
            Button(text=Const('05'), id='button_05', on_click=button_min_clicked),
            Button(text=Const('10'), id='button_10', on_click=button_min_clicked),),
        Row(
            Button(text=Const('15'), id='button_15', on_click=button_min_clicked),
            Button(text=Const('20'), id='button_20', on_click=button_min_clicked),
            Button(text=Const('25'), id='button_25', on_click=button_min_clicked), ),
        Row(
            Button(text=Const('30'), id='button_30', on_click=button_min_clicked),
            Button(text=Const('35'), id='button_35', on_click=button_min_clicked),
            Button(text=Const('40'), id='button_40', on_click=button_min_clicked), ),
        Row(
            Button(text=Const('45'), id='button_45', on_click=button_min_clicked),
            Button(text=Const('50'), id='button_50', on_click=button_min_clicked),
            Button(text=Const('55'), id='button_55', on_click=button_min_clicked), ),
        Row(
            Button(text=Const('Запустить'), id='zapusk', on_click=button_zapusk_clicked),
        ),

        state=FSM_ST.minuten,
    ),

    Window(
        Const(basic_menu),
        Button(text=Const('Напомнить мне !'),
              id='see_stelle_button',
              on_click=scheduler_job),
        state=FSM_ST.vor_mahnung,
    ),

    Window(
        Const('Напоминание принято'),
        Button(text=Const('Напомнить мне !'),
              id='see_stelle_button',
              on_click=go_to_next_dialog),
        state=FSM_ST.nach_mahnung_accepting,
    ),
)

mahnung_dialog = Dialog(
    Window(
        Const('Мы во втором диалоге'),
        state=MAHNUNG.mahnung_start,
    ),

    Window(
        Const('*****'),
        state=MAHNUNG.mahnung_gearbeitet,
    ),

    Window(  # Окно показывает виджет с мультиселектом
        Const(text='Отметьте свои скилы'),
        state=MAHNUNG.nach_mahnung,
        getter=get_skills
    ),

    # Window(
    #     Const('Отправьте фото в ответ'),
    #     Next(Const("Загрузить фото"),
    #          id="send_foto"),
    #     state=MAHNUNG.load_foto,
    # ),
    #
    # Window(  # Окно принимающее фото
    #     Const(text='Пришлите мне Ваше Фото 👦'),
    #     MessageInput(
    #         func=on_photo_sent,
    #         content_types=ContentType.PHOTO,
    #     ),
    #     MessageInput(
    #         func=message_not_foto_handler,
    #         content_types=ContentType.ANY,
    #     ),
    #     state=ANKETA.classic_handler
    # ),
    #
    # Window(
    #     Const('Данные приняты'),
    #     Next(Const('Сформировать анкету'), id='next2'),
    #     state=ANKETA.foto,
    # ),
    #
    # Window(
    #     Format(text='{capt}'),
    #     DynamicMedia("foto"),
    #     Start(Const('В основное меню ▶️'),
    #           id='go_to_basic',
    #           state=FSM_ST.basic,
    #           mode=StartMode.RESET_STACK),
    #     state=ANKETA.finish,
    # ),
)

vacancies = Dialog(
    Window(
        Const('В базе пока нет вакансий'),
        Start(Const('В основное меню ▶️'),
              id='go_to_basic',
              state=FSM_ST.vor_mahnung,
              mode=StartMode.RESET_STACK),
        state=VAC.empty,
    ), )
