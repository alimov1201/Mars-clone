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
lang = ['uz']

class New_student(StatesGroup):
    lang = State()
    name = State()
    age = State()
    phone_number = State()

class Form(StatesGroup):
    modemeID = State()

class Comment(StatesGroup):
    comment = State()

class Language(StatesGroup):
    language = State()

class Change_lang(StatesGroup):
    language = State()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Language.language)
    await message.answer(text='tilni tanlang \nвыберите язык', reply_markup=kb.lang_kb)

@router.message(F.text == '⚙️ изменить язык')
async def change_lang(message: Message, state: FSMContext):
    await state.set_state(Change_lang.language)
    await message.answer(text="выберите язык", reply_markup=kb.lang_kb)

@router.message(F.text == '⚙️ Tilni o`zgartirish')
async def change_lang_uz(message: Message, state: FSMContext):
    await state.set_state(Change_lang.language)
    await message.answer(text="Tilni tanlang", reply_markup=kb.lang_kb)

@router.message(Change_lang.language)
async def lang_ru(message: Message, state: FSMContext):
    global lang
    await state.clear()
    if lang[0]:
        lang.pop()
        lang.append(message.text)
    else:
        lang.append(message.text)
    if lang[0] == 'ru':
        await message.answer(text="язык изменен\nПожалуйста укажите кем вы являетесь", reply_markup=kb.indicator_person)
    else:
        await message.answer(text="Til o'zgartirildi\n Iltimos kimligingizni ko`rsating", reply_markup=kb.indicator_person_uz)

    

@router.message(Language.language)
async def language_function(message: Message, state: FSMContext):
    global lang
    if lang[0]:
        lang.pop()
        lang.append(message.text)
    else:
        lang.append(message.text)
    await state.clear()
    if lang[0] == 'ru':
        await message.answer(text="Добро пожаловать в Mars Bot!\nПожалуйста укажите кем вы являетесь", reply_markup=kb.indicator_person)
    else:
        await message.answer(text="Mars Botga xush kelibsiz \n Iltimos kimligingizni ko`rsating", reply_markup=kb.indicator_person_uz)

@router.callback_query(F.data == 'parent')
async def parent_cmd(call: CallbackQuery):
    await call.answer(text='you are parent')
    await call.message.answer(text='Добро пожаловать в Mars Bot! Пожалуйста, выберите вариант', reply_markup=kb.parent_kb)

@router.callback_query(F.data == 'parent_uz')
async def parent_cmd_uz(call: CallbackQuery):
    await call.answer(text='you are parent')
    await call.message.answer(text='Mars Botga xush kelibsiz! Iltimos, variantni tanlang', reply_markup=kb.parent_kb_uz)

@router.message(F.text == '🏫 О школе')
async def about_school(message: Message):
    await message.answer(text='Наш учебный центр превращает страсть к технологиям в полезное занятие, обучая детей создавать собственные игры и приложения, которые способствуют критическому мышлению и творчеству.\n\nМы предлагаем курсы программирования и дизайна, которые дополняют школьную программу и дают детям знания и навыки, необходимые для достижения успеха в будущем.')

@router.message(F.text == '🏫 O`quv markaz haqida')
async def about_school_uz(message: Message):
    await message.answer(text='Bizning o‘quv markazimiz bolalarni tanqidiy fikrlash va ijodkorlikni rivojlantiruvchi o‘z o‘yinlari va ilovalarini yaratishga o‘rgatish orqali texnologiyaga bo‘lgan ishtiyoqni foydali mashg‘ulotga aylantiradi.\n\nBiz maktab o‘quv dasturini to‘ldiradigan hamda bolalarga bilim va ko‘nikmalar beradigan dasturlash va dizayn kurslarini taklif etamiz. kelajakda muvaffaqiyatga erishish uchun kerak.')

@router.message(F.text == '📝 О наших курсах')
async def about_course(message: Message):
    await message.answer(text='занятия проводятся 3 раза в неделю. Полный курс 18 месяцев. Курс состоит из 3 модулей. каждый модуль длится 6 месяцев.\n\n12 уроков в месяц по 60 минут каждое. занятия в удобное время, выбранное согласно расписанию группы')

@router.message(F.text == '📝 Kurslarimiz haqida')
async def about_course_uz(message: Message):
    await message.answer(text='darslar haftasiga 3 marta o`tkaziladi. To`liq kurs 18 oy. Kurs 3 moduldan iborat. har bir modul 6 oy davom etadi.\n\nOyiga 12 ta dars, har biri 60 daqiqa. guruh jadvaliga muvofiq tanlangan qulay vaqtda darslar')

@router.message(F.text == '🔥 Работы наших учеников')
async def student_works(message: Message):
    await message.answer(text='Посмотреть работы наших учеников вы можете по ссылке ниже.\n https://t.me/studentsmars')

@router.message(F.text == '🔥 O`quvchilarimiz ishlari')
async def student_works_uz(message: Message):
    await message.answer(text='Talabalarimiz ishini quyidagi havola orqali ko`rishingiz mumkin.\n https://t.me/studentsmars')

@router.message(F.text == '☎️ Контакты и наши страницы')
async def our_site(message: Message):
    await message.answer(text='📍Филиал Юнусабад\nНомер телефон:\n+998901165054\n+998901175054\nнаш сайт - https://marsit.uz/')

@router.message(F.text == '☎️ Kontakt va ijtimoiy sahifalarimiz')
async def our_site_uz(message: Message):
    await message.answer(text='📍Yunusobod filiali\nTel:\n+998901165054\n+998901175054\nBizning sayt - https://marsit.uz/')

@router.message(F.text == '👨‍👩‍👦 Добавить ребёнка')
async def add_children(message: Message, state: FSMContext):
    await state.set_state(New_student.name)
    await message.answer(text='введите имя вашего ребенка')

@router.message(F.text == '👨‍👩‍👦 Farzand qo`shish')
async def add_children_uz(message: Message, state: FSMContext):
    await state.set_state(New_student.name)
    await message.answer(text='Farzandingiz ismini kiriting')

@router.message(New_student.name)
async def new_student_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(New_student.age)
    if lang[0] == 'ru':
        await message.answer(text='сколько лет вашему ребенку')
    else:
        await message.answer(text="Farzandingiz yoshi nechada")

@router.message(New_student.age)
async def new_student_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(New_student.phone_number)
    if lang[0] == 'ru':
        await message.answer(text="пришлите свой номер телефона", reply_markup=kb.phone_number)
    else:
        await message.answer(text="Telefon raqamingizni jo`nating", reply_markup=kb.phone_number)

@router.message(New_student.phone_number)
async def new_student_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    if lang[0] == 'ru':
        await message.answer(text="мы свяжемся с вами в ближайшее время", reply_markup=kb.parent_kb)
    else:
        await message.answer(text="Biz siz bilan yaqin orada bog`lanamiz", reply_markup=kb.parent_kb_uz)
    await state.clear()

@router.callback_query(F.data == 'guest')
async def guest_cmd(call: CallbackQuery):
    await call.answer(text='you are guest')
    await call.message.answer(text='Добро пожаловать в Mars Bot! Пожалуйста, выберите вариант', reply_markup=kb.guest_kb)

@router.callback_query(F.data == 'guest_uz')
async def guest_cmd_uz(call: CallbackQuery):
    await call.answer(text='you are guest')
    await call.message.answer(text='Mars Botga xush kelibsiz! Iltimos, variantni tanlang', reply_markup=kb.guest_kb_uz)

@router.message(F.text == '📍 Филиалы')
async def branches(message: Message):
    await message.answer(text='''
На данный момент у нас есть два филиала.

📍Филиал Тинчлик
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
    
@router.message(F.text == '📍 Filiallar')
async def branches_uz(message: Message):
    await message.answer(text='''
Ayni paytda bizda ikkita filial mavjud.

📍Tinchlik filiali
Manzil: Toshkent shahri, Tinchlik metro bekati, Beruniy 35 A
Telefon raqami:
+998954105054
+998954115054 

📍Yunusobod filiali
Manzil: Yunusobod tumani, Stroy markazi, 3-qavat.
Telefon raqami:
+998901165054
+998901175054

🗺 Filial manzilini quyidagi tugmalar orqali bilib olishingiz mumkin.''', reply_markup=kb.branches_uz)

@router.callback_query(F.data == 'yunusobod')
async def yunusobod(call: CallbackQuery):
    await call.answer(text='yunusobod')
    await call.message.answer_location(latitude=41.366922, longitude=69.285869)
    await call.message.answer(text='Юнусабад')

@router.callback_query(F.data == 'yunusobod_uz')
async def yunusobod_uz(call: CallbackQuery):
    await call.answer(text='yunusobod')
    await call.message.answer_location(latitude=41.366922, longitude=69.285869)
    await call.message.answer(text='Yunusobod')

@router.callback_query(F.data == 'tinchlik')
async def tinchlik(call: CallbackQuery):
    await call.answer(text='tinchlik')
    await call.message.answer_location(latitude=41.334779, longitude=69.215427)
    await call.message.answer(text='Тинчлик')

@router.callback_query(F.data == 'tinchlik_uz')
async def tinchlik_uz(call: CallbackQuery):
    await call.answer(text='tinchlik')
    await call.message.answer_location(latitude=41.334779, longitude=69.215427)
    await call.message.answer(text='Tinchlik')

@router.message(F.text == '💥 Space Shop')
async def space_shop(message: Message):
    await message.answer(text='Для покупки продукции перейдите на https://space.marsit.uz')

@router.message(F.text == '✍️ Оставить отзыв')
async def comment(message: Message, state: FSMContext):
    await state.set_state(Comment.comment)
    await message.answer(text='Напишите свой отзыв')

@router.message(F.text == '✍️ Izoh qoldirish')
async def comment_uz(message: Message, state: FSMContext):
    await state.set_state(Comment.comment)
    await message.answer(text='Izohingizni qoldiring')

@router.message(Comment.comment)
async def send_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    if lang[0] == 'ru':
        await message.answer(text='Спасибо что помогаете нам улучшатся', reply_markup=kb.student_kb)
    else:
        await message.answer(text='Bizni yaxshilashga yordam berganingiz uchun tashakkur', reply_markup=kb.student_kb_uz)
    await state.clear()


@router.callback_query(F.data == 'student')
async def student_cmd(call: CallbackQuery, state: FSMContext):
    await call.answer(text='you are student')
    await state.set_state(Form.modemeID)
    await call.message.answer(text="Введите свой modemeID")

@router.callback_query(F.data == 'student_uz')
async def student_cmd_uz(call: CallbackQuery, state: FSMContext):
    await call.answer(text='you are student')
    await state.set_state(Form.modemeID)
    await call.message.answer(text="'ModemID'ingizni kiriting")

@router.message(Form.modemeID)
async def student_profile(message: Message, state: FSMContext):
    await state.update_data(modemeID=message.text)
    state_data = await state.get_data()
    if student == []:
        student.append(message.text)
    modemeID = state_data['modemeID']
    async with aiohttp.ClientSession() as session:
        async with session.get('https://66f8f2852a683ce973107d51.mockapi.io/space') as response:
            if response.status == 200:
                data = await response.json()
                for item in data:
                    if str(item['modemeID']) == str(modemeID):
                        result = "\n".join([f"{item['modemeID']}: {item['full_name']}"])
                        if lang[0] == 'ru':
                            await message.answer(text=f"Полученные данные:\n{result}", reply_markup=kb.student_kb)
                        else:
                            await message.answer(text=f"Olingan ma'lumotlar:\n{result}", reply_markup=kb.student_kb_uz)
    await state.clear()

@router.message(F.text == "🧑‍🎓 Профиль")
async def student_info(message: Message):
    modem_id = student[0]
    async with aiohttp.ClientSession() as session:
        async with session.get('https://66f8f2852a683ce973107d51.mockapi.io/space') as response:
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

@router.message(F.text == "🧑‍🎓 Profil")
async def student_info_uz(message: Message):
    modem_id = student[0]
    async with aiohttp.ClientSession() as session:
        async with session.get('https://66ef9b6ef2a8bce81be3a011.mockapi.io/Mars') as response:
            if response.status == 200:
                data = await response.json()
                for item in data:
                    if str(item['modemeID']) == str(modem_id):
                        result = (f"modemeID: {item['modemeID']}\n"
                                    f"To'liq ism: {item['full_name']}\n"
                                    f"Filial: {item['fillial']}\n"
                                    f"Gruppa: {item['group']}\n"
                                    f"Liga: {item['liga']}\n"
                                    f"Coinlar: {item['coin']}")
                        await message.reply(text=result)

