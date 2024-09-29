from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

indicator_person = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='👨‍👩‍👦 я родитель', callback_data='parent'),
    InlineKeyboardButton(text='🧑‍🎓 Я студент', callback_data='student'),
    InlineKeyboardButton(text='👤 я гость', callback_data='guest')]
])

indicator_person_uz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='👨‍👩‍👦 Ota-onaman ', callback_data='parent_uz'),
    InlineKeyboardButton(text='🧑‍🎓 O`quvchiman', callback_data='student_uz'),
    InlineKeyboardButton(text='👤 Mehmonman', callback_data='guest_uz')]
])

branches = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Юнусабад', callback_data='yunusobod'), InlineKeyboardButton(text='Тинчлик', callback_data="tinchlik")]
])

branches_uz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Yunuobod', callback_data='yunusobod_uz'), InlineKeyboardButton(text='Tinchlik', callback_data="tinchlik_uz")]
])

parent_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📍 Филиалы'), KeyboardButton(text='🏫 О школе'), KeyboardButton(text='👨‍👩‍👦 Добавить ребёнка')],
    [KeyboardButton(text='🔥 Работы наших учеников'), KeyboardButton(text='📝 О наших курсах'), KeyboardButton(text='☎️ Контакты и наши страницы')],
    [KeyboardButton(text='⚙️ изменить язык')]
], resize_keyboard=True)

parent_kb_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📍 Filiallar'), KeyboardButton(text='🏫 O`quv markaz haqida'), KeyboardButton(text='👨‍👩‍👦 Farzand qo`shish')],
    [KeyboardButton(text='🔥 O`quvchilarimiz ishlari'), KeyboardButton(text='📝 Kurslarimiz haqida'), KeyboardButton(text='☎️ Kontakt va ijtimoiy sahifalarimiz')],
    [KeyboardButton(text='⚙️ Tilni o`zgartirish')]
], resize_keyboard=True)

guest_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📍 Филиалы'), KeyboardButton(text='📝 О наших курсах'), KeyboardButton(text='🔥 Работы наших учеников')],
    [KeyboardButton(text='🏫 О школе'), KeyboardButton(text='☎️ Контакты и наши страницы'), KeyboardButton(text='⚙️ изменить язык')]
], resize_keyboard=True)

guest_kb_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📍 Filiallar'), KeyboardButton(text='📝 Kurslarimiz haqida'), KeyboardButton(text='🔥 O`quvchilarimiz ishlari')],
    [KeyboardButton(text='🏫 O`quv markaz haqida'), KeyboardButton(text='☎️ Kontakt va ijtimoiy sahifalarimiz'), KeyboardButton(text='⚙️ Tilni o`zgartirish')]
], resize_keyboard=True)

student_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🧑‍🎓 Профиль'), KeyboardButton(text='💥 Space Shop'), KeyboardButton(text='🏫 О школе')],
    [KeyboardButton(text='✍️ Оставить отзыв'), KeyboardButton(text='⚙️ изменить язык')]
], resize_keyboard=True)

student_kb_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🧑‍🎓 Profil'), KeyboardButton(text='💥 Space Shop'), KeyboardButton(text='🏫 O`quv markaz haqida')],
    [KeyboardButton(text='✍️ Izoh qoldirish'), KeyboardButton(text='⚙️ Tilni o`zgartirish')]
], resize_keyboard=True)

phone_number = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='📞', request_contact=True)
    ]
], resize_keyboard=True)

lang_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="ru", ), KeyboardButton(text='uz')]
], resize_keyboard=True)
