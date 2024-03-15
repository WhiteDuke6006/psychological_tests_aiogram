import time
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import cung_test_keyboard, to_result_cung, cung_result
from core.handlers.basic import chat_text1
from core.handlers.basic import special

users_data = {}
deleter = {}
question = ['Навіть незначні зусилля виклиеають у мене втому', 'Іноді мені дуже легко заплакати', 'Мені часто буває досить сумно', 'Я відчуваю безсоння', 'Мені важко знайти вирішення проблем', 'Я не вірю у своє краще майбутнє', 'Тільки вранці/вечорами я відчуваю себе краще', 'Іноді моє серце починає битися швидше без особливої на те причини', 'Останнім часом я худну']

async def start_cung(message: Message, bot: Bot):
    deleter[message.from_user.id] = []
    deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, 'Останнім часом мене все дратує', reply_markup=cung_test_keyboard()))
    users_data[message.from_user.id] = [0, 0, 0]
    time.sleep(1)
    try:
        for i in special[message.from_user.id]:
            await i.delete()
        special.clear()
    except KeyError:
        pass
    await chat_text1[message.from_user.id].delete()


async def true_cung(message: Message, bot: Bot):
    users_data[message.from_user.id][0] += 1

    if users_data[message.from_user.id][1] != 9:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, f'{question[users_data[message.from_user.id][1]]}', reply_markup=cung_test_keyboard()))
    else:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, 'ПЕРЕГЛЯНУТИ РЕЗУЛЬТАТ 📈', reply_markup=to_result_cung()))

    users_data[message.from_user.id][1] += 1
    time.sleep(1)
    await deleter[message.from_user.id][-1].delete()
    deleter[message.from_user.id].pop()


async def false_cung(message: Message, bot: Bot):
    users_data[message.from_user.id][0] -= 1

    if users_data[message.from_user.id][1] != 9:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, f'{question[users_data[message.from_user.id][1]]}', reply_markup=cung_test_keyboard()))
    else:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, 'ПЕРЕГЛЯНУТИ РЕЗУЛЬТАТ 📈', reply_markup=to_result_cung()))

    users_data[message.from_user.id][1] += 1
    time.sleep(1)
    await deleter[message.from_user.id][-1].delete()
    deleter[message.from_user.id].pop()


async def get_cung_result(message: Message, bot: Bot):
    if users_data[message.from_user.id][0] >= 5:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, 'У вас підвищена тривожність !', reply_markup=cung_result()))
    else:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, 'Рівень тривожності у нормі, але краще звернутися до спеціалістів !', reply_markup=cung_result()))

    await deleter[message.from_user.id][-1].delete()
    deleter[message.from_user.id].pop()


