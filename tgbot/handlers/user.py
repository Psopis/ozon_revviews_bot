import time

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import tortoise
from tgbot.keyboards.inline import start_keyboard, registrtion_keyboard, add_rule_text_messaging, change_rule_messaging, \
    stop_words, otziv, trafis_choose
from aiogram.types import CallbackQuery
from tgbot.models import User, User_text


class Form(StatesGroup):
    serial_user = State()
    messaging_rule = State()
    stop_word = State()
    otziv = State()


async def user_start(message: Message):
    await message.answer("""Благодарим за проявленный интерес к 
нашему сервису. Наш сервис создан для
упрощения вашей рутинной работы и
ответов за Вас на отзывы Ваших
клиентов используя в своей работе
искусственный интеллект. Выберите
один из пунктов меню для продолжения
работы:""", reply_markup=start_keyboard())


async def what_our_bot_can_do(call: CallbackQuery):
    await call.answer()
    await call.message.answer("""1. Умеет обрабатывать отзывы 
клиентов из личного кабинета 
Вашего магазина на Озон. Читать их, 
формировать и публиковать ответы 
на них.""")
    await call.message.answer("""2. Умеет присылать Вам его вариант 
ответа на отзыв, если отзыв 
содержит вопрос от клиента или 
стоп-слова, которые Вы указали. Вы 
можете либо оставить его вариант 
ответа и согласовать публикацию,
либо выслать ему свой вариант""")
    await call.message.answer("""3. Умеет обучаться. Вы можете задать 
ему правила ответов на отзывы (мы 
покажем Вам наш вариант, Вы 
можете его скорректировать). Бот 
будет отвечать на отзывы на 
основании этих правил""")
    await call.message.answer("""4. Умеет присылать статистику по 
отзывам. Сколько отзывов было 
получено за месяц, за неделю, за 
день. Какие товары чаще получают 
негативные отзывы, какие 
положительные""", reply_markup=start_keyboard())


async def registration_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("Пожалуйста укажите Ваш seller ID")
    await state.set_state(Form.serial_user)


async def registration_handler_sec(message: Message, state: FSMContext):
    user_id = message.text
    print(user_id)
    user = User(user_id=user_id, shop_id=0)
    await user.save()

    await message.answer("""Благодарим. Для получения доступа к Вашим 
отзывам Вам необходимо добавить нашего 
бота в качестве сотрудника в свой магазин в 
личном кабинете Озон (подробную 
инструкцию можно посмотреть тут)
e-mail: otvechy_sam_bot@yandex.ru
роль: Менеджер по товарам
После того, как Вы добавите нашего бота как 
сотрудника ему понадобится немного 
времени чтобы получить доступ к отзывам и 
начать их загружать. По готовности он Вам 
напишет.""", reply_markup=registrtion_keyboard())
    await state.finish()
    await state.update_data(user_id=user_id)
    print(1)


async def tarifs_handler(call: CallbackQuery):
    await call.message.answer("""Пробный период 14 дней с ограничением в 
150 ответов на отзывы. При подключении 
подписки ограничений на отзывы нет
• Подписка на 14 дней – 249р.
• Подписка на 30 дней – 399р.""", reply_markup=trafis_choose())


async def tarifs_for_14_handler(call: CallbackQuery):
    await call.message.answer("Вы оформили на 14 дней")
    await call.message.answer("""Благодарим за проявленный интерес к 
        нашему сервису. Наш сервис создан для
        упрощения вашей рутинной работы и
        ответов за Вас на отзывы Ваших
        клиентов используя в своей работе
        искусственный интеллект. Выберите
        один из пунктов меню для продолжения
        работы:""", reply_markup=start_keyboard())


async def tarifs_for_30_handler(call: CallbackQuery):
    await call.message.answer("Вы оформили на 30 дней")
    await call.message.answer("""Благодарим за проявленный интерес к 
        нашему сервису. Наш сервис создан для
        упрощения вашей рутинной работы и
        ответов за Вас на отзывы Ваших
        клиентов используя в своей работе
        искусственный интеллект. Выберите
        один из пунктов меню для продолжения
        работы:""", reply_markup=start_keyboard())


async def main_menu_handler(call: CallbackQuery):
    await call.message.answer("""Благодарим за проявленный интерес к 
    нашему сервису. Наш сервис создан для
    упрощения вашей рутинной работы и
    ответов за Вас на отзывы Ваших
    клиентов используя в своей работе
    искусственный интеллект. Выберите
    один из пунктов меню для продолжения
    работы:""", reply_markup=start_keyboard())


async def add_employee_handler(call: CallbackQuery):
    print(2)
    await call.answer()
    await call.message.answer("Благодарим. Ожидайте сообщения от бота.")
    time.sleep(4)
    await call.message.answer("""Благодарю за ожидание. Я загрузил 212 
отзывов по магазину inSocks и готов приступить 
к ответам на них. Задай для меня правила 
общения, задай стоп-слова и выбери отзывы, 
ответы на которые мне нужно согласовать с 
тобой. И так, давай по порядку""", reply_markup=add_rule_text_messaging())


async def add_rule_message_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    text = """Твоя роль – менеджер маркетплейса. Ты 
отвечаешь на отзывы клиентов. При ответах 
всегда обращайся к клиенту на «Вы», 
используй только уважительную форму 
ответа. Всегда выражай готовность помочь и 
предлагай связаться с нами в чате, в случае 
если у клиента появятся вопросы. Старайся 
обращаться по имени, если имя клиента 
написано на русском языке, если же нет, 
просто используй уважительную форму 
обращения. В отзывах, где клиент остался 
недоволен, старайся добавлять подпись «С 
Уважением, команда магазина *»
Где * будет соответствовать тому магазину, в 
котором ты отвечаешь на отзыв
"""
    await call.message.answer("Вот какие правила действуют для меня по умолчанию:")
    await call.message.answer(text, reply_markup=change_rule_messaging())


async def change_rule_message_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("Задать свои")
    await state.set_state(Form.messaging_rule)


async def change_rule_message_handler_second(message: Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    user_id = data.get('user_id')


    await message.answer("Вы задали правило")
    await message.answer(text, reply_markup=change_rule_messaging())
    await state.finish()
    await state.update_data(user_id=user_id)
    await state.update_data(message_rule=text)


async def not_change_rule_message_handler_second(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Задайте стоп слова", reply_markup=stop_words())


async def add_bad_words_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("""Если я буду встречать данные слова и их 
склонения в тексте отзыва клиента, я буду 
формировать ответ на отзыв, но публикацию 
согласую с тобой. Пришли мне слова через 
запятую, в одном сообщении. Если по ходу 
работы захочешь добавить или изменить их, ты 
всегда сможешь сделать это через Настройки""")
    await state.set_state(Form.stop_word)


async def change_bad_words_handler_second(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("Пришли мне новые стоп-слова через запятую, в одном сообщении")
    await state.set_state(Form.stop_word)


async def add_bad_words_handler_second(message: Message, state: FSMContext):
    text = message.text
    print(text.split(","))
    data = await state.get_data()
    user_id = data.get('user_id')
    message_rule = data.get('message_rule')

    await message.answer(f"Вы задали \n{text}", reply_markup=stop_words())
    await state.finish()
    await state.update_data(user_id=user_id)
    await state.update_data(message_rule=message_rule)
    await state.update_data(stop_words=text)


async def choose_otziv_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("""Укажи через запятую оценки отзывов, которые 
требую согласования перед ответом. Например: 
1, 2. Так я буду формировать ответы на все 
отзывы с оценками 1 и 2 и согласовывать 
публикацию
""")
    await state.set_state(Form.otziv)


async def change_choose_otziv_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("""Для замены укажи через запятую оценки отзывов, которые 
требую согласования перед ответом.""")
    await state.set_state(Form.otziv)


async def choose_otziv_handler_second(message: Message, state: FSMContext):
    text = message.text
    print(text.split(","))
    data = await state.get_data()
    user_id = data.get('user_id')
    message_rule = data.get('message_rule')
    stop_words = data.get('stop_words')
    print(user_id)
    print(message_rule)
    print(stop_words)
    user_text = User_text(user_id=user_id, message_rule=message_rule, stop_word=stop_words, otziv=text)
    await user_text.save()
    await message.answer("Отзывы", reply_markup=otziv())
    await state.finish()


async def start_work_handler(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("""Благодарю за оказанное доверие. Я пришлю 
свои первые 10 ответов на отзывы на 
согласование, чтобы ты проверил мои ответы. 
Если все 10 ответов будут согласованы дальше 
моя работа будет автоматической. Если же хоть 
один из ответов не будет согласован, 
пожалуйста измени правила моего общения, и 
я начну с начала""")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_callback_query_handler(what_our_bot_can_do, text="what_can_bot_do")
    dp.register_callback_query_handler(registration_handler, text="user_registration")
    dp.register_message_handler(registration_handler_sec, state=Form.serial_user)
    dp.register_callback_query_handler(add_employee_handler, text="add_employee")
    dp.register_callback_query_handler(tarifs_handler, text="tarifs")
    dp.register_callback_query_handler(tarifs_for_14_handler, text="tarifs_for_14")
    dp.register_callback_query_handler(tarifs_for_30_handler, text="tarifs_for_30")
    dp.register_callback_query_handler(main_menu_handler, text="main_menu")

    dp.register_callback_query_handler(add_rule_message_handler, text="add_rule")
    dp.register_callback_query_handler(change_rule_message_handler, text="change_rule_messaging")
    dp.register_message_handler(change_rule_message_handler_second, state=Form.messaging_rule)
    dp.register_callback_query_handler(not_change_rule_message_handler_second, text="not_change_rule_messaging")
    dp.register_callback_query_handler(add_bad_words_handler, text="add_stop_words")
    dp.register_message_handler(add_bad_words_handler_second, state=Form.stop_word)
    dp.register_callback_query_handler(change_bad_words_handler_second, text="change_stop_words")
    dp.register_callback_query_handler(choose_otziv_handler, text="choose_otziv")
    dp.register_callback_query_handler(change_choose_otziv_handler, text="change_otzivs")
    dp.register_message_handler(choose_otziv_handler_second, state=Form.otziv)
