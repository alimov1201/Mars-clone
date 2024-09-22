from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

indicator_person = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='👨‍👩‍👦 я родитель', callback_data='parent'),
    InlineKeyboardButton(text='🧑‍🎓 Я студент', callback_data='student'),
    InlineKeyboardButton(text='👤 я гость', callback_data='guest')]
])

branches = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Юнусабад', callback_data='yunusobod'), InlineKeyboardButton(text='Тинчлик', callback_data="tinchlik")]
])

parent_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📍 Филиалы'), KeyboardButton(text='🏫 О школе'), KeyboardButton(text='👨‍👩‍👦 Добавить ребёнка')],
    [KeyboardButton(text='🔥 Работы наших учеников'), KeyboardButton(text='📝 О наших курсах'), KeyboardButton(text='☎️ Контакты и наши страницы')]
], resize_keyboard=True)

guest_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📍 Филиалы'), KeyboardButton(text='📝 О наших курсах'), KeyboardButton(text='🔥 Работы наших учеников')],
    [KeyboardButton(text='🏫 О школе'), KeyboardButton(text='☎️ Контакты и наши страницы')]
], resize_keyboard=True)

student_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🧑‍🎓 Профиль'), KeyboardButton(text='💥 Space Shop'), KeyboardButton(text='🏫 О школе')],
    [KeyboardButton(text='✍️ Оставить отзыв')]
], resize_keyboard=True)

phone_number = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='📞', request_contact=True)
    ]
], resize_keyboard=True)
