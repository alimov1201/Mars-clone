from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
import aiohttp
import json

router = Router()
student = []

class New_student(StatesGroup):
    name = State()
    age = State()
    phone_number = State()

class Form(StatesGroup):
    modemeID = State()

class Comment(StatesGroup):
    comment = State()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text="Добро пожаловать в Mars Bot!\nПожалуйста укажите кем вы являетесь", reply_markup=kb.indicator_person)

@router.callback_query(F.data == 'parent')
async def parent_cmd(call: CallbackQuery):
    await call.answer(text='you are parent')
    await call.message.answer(text='Добро пожаловать в Mars Bot! Пожалуйста, выберите вариант', reply_markup=kb.parent_kb)

@router.message(F.text == '🏫 О школе')
async def about_school(message: Message):
    await message.answer(text='Наш учебный центр превращает страсть к технологиям в полезное занятие, обучая детей создавать собственные игры и приложения, которые способствуют критическому мышлению и творчеству.\n\nМы предлагаем курсы программирования и дизайна, которые дополняют школьную программу и дают детям знания и навыки, необходимые для достижения успеха в будущем.')

@router.message(F.text == '📝 О наших курсах')
async def about_course(message: Message):
    await message.answer(text='занятия проводятся 3 раза в неделю. Полный курс 18 месяцев. Курс состоит из 3 модулей. каждый модуль длится 6 месяцев.\n\n12 уроков в месяц по 60 минут каждое. занятия в удобное время, выбранное согласно расписанию группы')

@router.message(F.text == '🔥 Работы наших учеников')
async def student_works(message: Message):
    await message.answer(text='Посмотреть работы наших учеников вы можете по ссылке ниже.\n https://t.me/studentsmars')

@router.message(F.text == '☎️ Контакты и наши страницы')
async def our_site(message: Message):
    await message.answer(text='📍Филиал Юнусабад\nНомер телефон:\n+998901165054\n+998901175054\nнаш сайт - https://marsit.uz/')

@router.message(F.text == '👨‍👩‍👦 Добавить ребёнка')
async def add_children(message: Message, state: FSMContext):
    await state.set_state(New_student.name)
    await message.answer(text='введите имя вашего ребенка')

@router.message(New_student.name)
async def new_student_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(New_student.age)
    await message.answer(text='сколько лет вашему ребенку')

@router.message(New_student.age)
async def new_student_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(New_student.phone_number)
    await message.answer(text="пришлите свой номер телефона", reply_markup=kb.phone_number)

@router.message(New_student.phone_number)
async def new_student_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    await message.answer(text="мы свяжемся с вами в ближайшее время", reply_markup=kb.parent_kb)
    await state.clear()

@router.callback_query(F.data == 'guest')
async def guest_cmd(call: CallbackQuery):
    await call.answer(text='you are guest')
    await call.message.answer(text='Добро пожаловать в Mars Bot! Пожалуйста, выберите вариант', reply_markup=kb.guest_kb)

@router.message(F.text == '📍 Филиалы')
async def branches(message: Message):
    await message.answer(text='''
На данный момент у нас есть два филиала.

📍Отделение Тинчлик
Адрес: город Ташкент, метро Тинчлик, Беруний 35 А
Номер телефона:
+998954105054
+998954115054 

📍Филиал Юнусабад
Адрес: Юнусабадский район, Строй центр, 3 этаж.
Номер телефон:
+998901165054
+998901175054

🗺 Адрес филиала вы можете узнать, воспользовавшись кнопками ниже.''', reply_markup=kb.branches)

@router.callback_query(F.data == 'yunusobod')
async def yunusobod(call: CallbackQuery):
    await call.answer(text='yunusobod')
    await call.message.answer_location(latitude=41.366922, longitude=69.285869)
    await call.message.answer(text='Юнусабад')

@router.callback_query(F.data == 'tinchlik')
async def tinchlik(call: CallbackQuery):
    await call.answer(text='tinchlik')
    await call.message.answer_location(latitude=41.334779, longitude=69.215427)
    await call.message.answer(text='Тинчлик')

@router.message(F.text == '💥 Space Shop')
async def space_shop(message: Message):
    await message.answer(text='Для покупки продукции перейдите на https://space.marsit.uz')

@router.message(F.text == '✍️ Оставить отзыв')
async def comment(message: Message, state: FSMContext):
    await state.set_state(Comment.comment)
    await message.answer(text='Напишите свой отзыв')

@router.message(Comment.comment)
async def send_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await message.answer(text='Спасибо что помогаете нам улучшатся', reply_markup=kb.student_kb)
    await state.clear()


@router.callback_query(F.data == 'student')
async def student_cmd(call: CallbackQuery, state: FSMContext):
    await call.answer(text='you are student')
    await state.set_state(Form.modemeID)
    await call.message.answer(text="Введите свой modemeID")

@router.message(Form.modemeID)
async def student_profile(message: Message, state: FSMContext):
    await state.update_data(modemeID=message.text)
    state_data = await state.get_data()
    if student == []:
        student.append(message.text)
    modemeID = state_data['modemeID']
    async with aiohttp.ClientSession() as session:
        async with session.get('https://66ef9b6ef2a8bce81be3a011.mockapi.io/Mars') as response:
            if response.status == 200:
                data = await response.json()
                for item in data:
                    if str(item['modemeID']) == str(modemeID):
                        result = "\n".join([f"{item['modemeID']}: {item['full_name']}"])
                        await message.answer(text=f"Полученные данные:\n{result}", reply_markup=kb.student_kb)
    await state.clear()

@router.message(F.text == "🧑‍🎓 Профиль")
async def student_info(message: Message):
    modem_id = student[0]
    async with aiohttp.ClientSession() as session:
        async with session.get('https://66ef9b6ef2a8bce81be3a011.mockapi.io/Mars') as response:
            if response.status == 200:
                data = await response.json()
                for item in data:
                    if str(item['modemeID']) == str(modem_id):
                        result = (f"modemeID: {item['modemeID']}\n"
                                    f"полное имя: {item['full_name']}\n"
                                    f"Филиал: {item['fillial']}\n"
                                    f"группа: {item['group']}\n"
                                    f"лига: {item['liga']}\n"
                                    f"монеты: {item['coin']}")
                        await message.reply(text=result)


