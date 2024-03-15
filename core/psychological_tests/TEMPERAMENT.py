import time
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import temperament_test_keyboard, to_result_temperament, back_from_result
from core.handlers.basic import chat_text1
from core.handlers.basic import special

users_data = {}
deleter = {}
question = ['Ви активні та енергійні ?', 'Вам важко зосередитися на одній справі ?', 'Ви вважаєте себе рішучою людиною ?', 'Ви швидко втомлюєтеся від монотонних справ ?', 'Ви схильні до переживань ?', 'Ви швидко втомлюєтеся від шумних та активних заходів ?', 'Ви вважаєте себе чутливою особистістю ?', 'Ви схильні до творчого самовираження (малювання, письмо, музика) ?', 'Вас легко розгубити, чи збити з пантелику ?', 'Вам не подобається змінювати плани в останній момент ?', 'Ви зазвичай уникаєте конфліктних ситуацій ?', 'Ви вважаєте себе людиною з великою терплячістю ?', 'Вам подобається стабільність ?', 'Ви спокійно реагуєтe на труднощі ?', 'Ви зазвичай веселі та енергійні ?', 'Ви легко заводите нових друзів ?', 'Ви емоційно реагуєте на події навколо ?', 'Ви вважаєте себе оптимістичною людиною ?', 'Вам легко зосередитися на одній справі ?']

temperaments_info = {'Choleric': 'Холерик - це тип темпераменту, характеризується енергійністю, легко роздратовується та швидко реагує на подразники. Холерики часто є емоційно виразними, впертими і рішучими. Вони швидко приймають рішення, але можуть бути не терплячими з іншими людьми. Такі особи часто бувають лідерами в групі або команді, завдяки ',
                     'Melancholic': "Меланхолік - це тип темпераменту, який характеризується великою чутливістю, внутрішніми переживаннями і схильністю до задумливості. Меланхоліки часто мають тенденцію до підвищеної тривожності, схильні до роздумів та поглибленого аналізу. Вони можуть бути творчо обдарованими і віддані своїм ідеалам, але також схильні до перфекціонізму та підвищеної самокритичності. Меланхоліки шукають глибоких емоційних зв'язків і можуть бути вразливими у відносинах з іншими людьми.",
                     'Phlegmatic': "Флегматик - це тип темпераменту, що характеризується спокійністю, збалансованістю та стабільністю. Флегматики мають тенденцію до спокійних та розсудливих реакцій на події, їм не подобається драматизувати ситуації. Вони часто є надійними та стійкими в трудних ситуаціях, мають здатність до логічного мислення і розуміння деталей. Флегматики можуть бути менш емоційно виразними, але це не означає, що вони не відчувають емоції - вони просто виявляють їх менше в публічних ситуаціях.",
                     'Sanguine': "Сангвінік - це тип темпераменту, який характеризується життєрадісністю, енергійністю та оптимізмом. Сангвініки часто є спонтанними і комунікабельними, люблять бути в центрі уваги та веселити інших. Вони легко входять у контакт з новими людьми і часто мають багато друзів. Сангвініки можуть бути витонченими говорунами та легко знаходять спільну мову з будь-якими людьми. Вони швидко відновлюють оптимізм після негативних ситуацій і зазвичай бачать в них можливості для розвитку."}

temperaments_photos = {'Choleric': "AgACAgIAAxkBAAINf2XzJEDVXmtZP5EEZKaMOFirK1B0AAJV2DEbzfGZS62s1p8HURz6AQADAgADeQADNAQ",
                       'Melancholic': "AgACAgIAAxkBAAINfGXzJC_hELJkF1K2n8tvhYSUR3HNAAJS2DEbzfGZS4kG1-hker3uAQADAgADeQADNAQ",
                       'Phlegmatic': "AgACAgIAAxkBAAINfWXzJDOR4OAenlJPQiD6a1ghg2UeAAJT2DEbzfGZS8Yx8DtgJK3YAQADAgADeQADNAQ",
                       'Sanguine': "AgACAgIAAxkBAAINfmXzJDaL_sTdSgGKYI63e8jwa9bSAAJU2DEbzfGZS7qbV3ZL9NYSAQADAgADeQADNAQ"}


async def start_temperament(message: Message, bot: Bot):
    deleter[message.from_user.id] = []
    deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, 'Ви легко дратуєтеся', reply_markup=temperament_test_keyboard()))
    users_data[message.from_user.id] = [0, 0, 0, 0, 0]
    time.sleep(1)
    try:
        for i in special[message.from_user.id]:
            await i.delete()
        special.clear()
    except KeyError:
        pass
    await chat_text1[message.from_user.id].delete()


async def true(message: Message, bot: Bot):
    if users_data[message.from_user.id][4] < 5:
        users_data[message.from_user.id][0] += 1
    elif users_data[message.from_user.id][4] < 10:
        users_data[message.from_user.id][1] += 1
    elif users_data[message.from_user.id][4] < 15:
        users_data[message.from_user.id][2] += 1
    elif users_data[message.from_user.id][4] < 20:
        users_data[message.from_user.id][3] += 1

    if users_data[message.from_user.id][4] != 19:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, f'{question[users_data[message.from_user.id][4]]}', reply_markup=temperament_test_keyboard()))
    else:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, 'ПЕРЕГЛЯНУТИ РЕЗУЛЬТАТ 📈', reply_markup=to_result_temperament()))

    users_data[message.from_user.id][4] += 1
    time.sleep(1)
    await deleter[message.from_user.id][-1].delete()
    deleter[message.from_user.id].pop()


async def false(message: Message, bot: Bot):
    if users_data[message.from_user.id][4] != 19:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, f'{question[users_data[message.from_user.id][4]]}', reply_markup=temperament_test_keyboard()))
    else:
        deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, 'ПЕРЕГЛЯНУТИ РЕЗУЛЬТАТ 📈', reply_markup=to_result_temperament()))

    users_data[message.from_user.id][4] += 1
    time.sleep(1)
    await deleter[message.from_user.id][-1].delete()
    deleter[message.from_user.id].pop()


async def get_temperament_result(message: Message, bot: Bot):
    result = {}
    result_temperament = {}
    result_temperament[message.from_user.id] = {}
    result_temperament[message.from_user.id]['Choleric'] = users_data[message.from_user.id][0]
    result_temperament[message.from_user.id]['Melancholic'] = users_data[message.from_user.id][1]
    result_temperament[message.from_user.id]['Phlegmatic'] = users_data[message.from_user.id][2]
    result_temperament[message.from_user.id]['Sanguine'] = users_data[message.from_user.id][3]
    result[message.from_user.id] = max(result_temperament[message.from_user.id], key=lambda x: result_temperament[message.from_user.id][x])
    deleter[message.from_user.id].insert(0, await bot.send_message(message.from_user.id, temperaments_info[result[message.from_user.id]]))
    deleter[message.from_user.id].insert(0, await bot.send_photo(message.from_user.id, photo=temperaments_photos[result[message.from_user.id]], reply_markup=back_from_result()))
    time.sleep(1)
    await deleter[message.from_user.id][-1].delete()
    deleter[message.from_user.id].pop()


