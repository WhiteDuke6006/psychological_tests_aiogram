from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_message_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Перейти до тестів🎯', callback_data='all_tests')
    keyboard_builder.button(text='Знайшли помилку🤔', url='tg://user?id=6565804926')

    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()



def all_tests():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🌠MBTI (тест на 1 з 16 типів особистості)🌌', callback_data='mbti')
    keyboard_builder.button(text='Тест на темперамент 😡😭🥱😊', callback_data='temperament')
    keyboard_builder.button(text='🤒Шкала Цунга (тест на депресію)🙁', callback_data='cung')
    keyboard_builder.button(text='🔥Тест Рокича (визначає цінності)🔥', callback_data='rockich')
    keyboard_builder.button(text='🔙 Назад...', callback_data='back')

    keyboard_builder.adjust(1, 1, 1, 1, 1)
    return keyboard_builder.as_markup()


def mbti_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='✅РОЗПОЧАТИ ТЕСТ✅', callback_data='start_mbti')
    keyboard_builder.button(text='❔ДЕТАЛЬНІШЕ❔', callback_data='detail_mbti')
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')

    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()



def temporarily_unavailable_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def detail_mbti_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='✅РОЗПОЧАТИ ТЕСТ✅', callback_data='start_mbti')
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()



def mbti_test_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🌀Це точно про мене💯', callback_data='100true')
    keyboard_builder.button(text='🌀Це про мене 👍🏻', callback_data='50true')
    keyboard_builder.button(text='🌀Швидше так 🙂', callback_data='25true')
    keyboard_builder.button(text='🌀Важко відповісти 😐', callback_data='none')
    keyboard_builder.button(text='🌀Швидше ні 🙁', callback_data='25false')
    keyboard_builder.button(text='🌀Це не про мене 👎🏻', callback_data='50false')
    keyboard_builder.button(text='🌀Це точно не про мене🙅🏻', callback_data='100false')
    keyboard_builder.button(text='   ❌ВИЙТИ❌', callback_data='exit')

    keyboard_builder.adjust(1, 1, 1, 1, 1)
    return keyboard_builder.as_markup()


def to_result_mbti_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='ДАЛІ✅', callback_data='to_result_mbti')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def back_from_result():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()



def temperament_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='✅РОЗПОЧАТИ ТЕСТ✅', callback_data='start_temperament')
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def temperament_test_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='ТАК', callback_data='true')
    keyboard_builder.button(text='НІ', callback_data='false')
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')
    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()

def to_result_temperament():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='ДАЛІ✅', callback_data='to_result_temperament')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()



def cung_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='✅РОЗПОЧАТИ ТЕСТ✅', callback_data='start_cung')
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()

def cung_test_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='ТАК', callback_data='true_cung')
    keyboard_builder.button(text='НІ', callback_data='false_cung')
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')
    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()

def to_result_cung():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='ДАЛІ✅', callback_data='to_result_cung')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def cung_result():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Звернутися за допомогою', url="https://www.rozmova.me/?utm_source=google&utm_medium=cpc&utm_campaign=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA.%D0%9F%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3.%D0%92%D1%81%D1%8F%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0.%D0%A8%D0%B8%D1%80%D0%BE%D0%BA%D0%BE%D0%B5.%D0%B4%D0%BE%D0%BF1&utm_term=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BC%D0%BE%D0%B3%D0%B0%20%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B0&position=&device=c&gad_source=1&gclid=CjwKCAjw48-vBhBbEiwAzqrZVMckVp_TA9tZcTMcTlfHAay4L4iTewU_xSb54zGOg_NF9V_cogsF3hoCgQMQAvD_BwE")
    keyboard_builder.button(text='❌ВИЙТИ❌', callback_data='exit')
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()