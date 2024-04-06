from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Что умеет наш бот?", callback_data="what_can_bot_do"))
    keyboard.add(InlineKeyboardButton(text="Регистрация", callback_data="user_registration"))
    keyboard.add(InlineKeyboardButton(text="Тарифы", callback_data="tarifs"))
    return keyboard


def registrtion_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Добавить магазин", callback_data="add_shop"))
    keyboard.add(InlineKeyboardButton(text="Сотрудник добавлен", callback_data="add_employee"))
    return keyboard


def trafis_choose():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Оформить на 14 дней", callback_data="tarifs_for_14"))
    keyboard.add(InlineKeyboardButton(text="Оформить на 30 дней", callback_data="tarifs_for_30"))
    keyboard.add(InlineKeyboardButton(text="Меню", callback_data="main_menu"))
    return keyboard


def add_rule_text_messaging():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Задать правила общения", callback_data="add_rule"))

    return keyboard


def change_rule_messaging():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Оставить текущие правила", callback_data="not_change_rule_messaging"))
    keyboard.add(InlineKeyboardButton(text="Задать свои", callback_data="change_rule_messaging"))

    return keyboard


def stop_words():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Задать стоп-словa", callback_data="add_stop_words"))
    keyboard.add(InlineKeyboardButton(text="Изменить список стоп-слов", callback_data="change_stop_words"))
    keyboard.add(InlineKeyboardButton(text="Выбери отзывы для согласования", callback_data="choose_otziv"))
    return keyboard


def otziv():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Выбери отзывы для согласования", callback_data="choose_otzivs"))
    keyboard.add(InlineKeyboardButton(text="Изменить отзывы для согласования", callback_data="change_otzivs"))
    keyboard.add(InlineKeyboardButton(text="Начать работу", callback_data="start_work"))
    return keyboard
