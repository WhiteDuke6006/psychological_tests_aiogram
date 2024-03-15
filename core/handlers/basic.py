import time
from core.utils.commands import set_commands
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import start_message_inline_keyboard, all_tests, mbti_keyboard, temporarily_unavailable_keyboard, detail_mbti_keyboard, temperament_keyboard, cung_keyboard

chat_text1 = {}
chat_text2 = {}
special = {}

async def start_message(message: Message, bot: Bot):
    chat_text1[message.from_user.id] = await bot.send_message(message.from_user.id, '👋 Привіт !!!\nЯ - твій віртуальний психолог, готовий допомогти тобі розкрити та зрозуміти свої внутрішні можливості. 💙💛\nЗ моєю допомогою ти зможеш пройти цікаві тести, які допоможуть виявити твої сильні сторони, розкрити потенційні можливості та розібратися у власних емоціях. 😉✨\nДавай разом відправимося у захопливу подорож в світ самопізнання та розвитку !\n🌠🌌', reply_markup=start_message_inline_keyboard())
    time.sleep(1)
    try:
       await chat_text2[message.from_user.id].delete()
    except KeyError:
        pass

    await set_commands(bot)
    await message.delete()


async def tests(message: Message, bot: Bot):
    chat_text2[message.from_user.id] = await bot.send_message(message.from_user.id, '\t📋Тести:', reply_markup=all_tests())
    time.sleep(1)
    try:
        from core.psychological_tests.CUNGA import deleter
        for i in deleter[message.from_user.id]:
            await i.delete()
        deleter[message.from_user.id].clear()
    except KeyError:
        pass
    try:
        from core.psychological_tests.TEMPERAMENT import deleter
        for i in deleter[message.from_user.id]:
            await i.delete()
        deleter[message.from_user.id].clear()
    except KeyError:
        pass
    try:
        from core.psychological_tests.MBTI import deleter
        for i in deleter[message.from_user.id]:
            await i.delete()
        deleter[message.from_user.id].clear()
    except KeyError:
        pass
    try:
        for i in special[message.from_user.id]:
            await i.delete()
        special.clear()
    except KeyError:
        pass
    await chat_text1[message.from_user.id].delete()


async def mbti(message: Message, bot: Bot):
    chat_text1[message.from_user.id] = await bot.send_message(message.from_user.id, 'MBTI (Myers-Briggs Type Indicator) - це психологічний тест, що визначає особистісні типи на основі чотирьох протилежних показників:\n\nЕкстраверсія (E) vs Інтроверсія (I),\nСприйняття (S) vs Інтуїція\n(N)Мислення (T) vs Відчуття (F)\nСудження (J) vs Пізнання (P)\n\nКожен тип має унікальні характеристики та представляє певний спосіб мислення, взаємодії з оточуючим світом та прийняття рішень.' , reply_markup=mbti_keyboard())
    time.sleep(1)
    await chat_text2[message.from_user.id].delete()


async def temporarily_unavailable(message: Message, bot: Bot):
    chat_text1[message.from_user.id] = await bot.send_message(message.from_user.id, '️❗Тимчасово Недоступний❗', reply_markup=temporarily_unavailable_keyboard())
    time.sleep(1)
    await chat_text2[message.from_user.id].delete()



async def detail_mbti(message: Message,bot: Bot):
    special[message.from_user.id] = []
    special[message.from_user.id].append(await bot.send_message(message.from_user.id, 'MBTI (Myers-Briggs Type Indicator) - це психологічний інструмент, розроблений Катріною Кук-Бріггс та Ізабеллою Бріггс-Майерс на основі роботи Карла Юнга, який допомагає визначити особистісні типи людей. Тест базується на чотирьох протилежних показниках:',))
    special[message.from_user.id].append(await bot.send_message(message.from_user.id, '1. Екстраверсія (E) vs Інтроверсія (I): \nЕкстраверти активно спілкуються з оточуючими та енергію черпають із зовнішніх джерел, в той час як інтроверти більш схильні до внутрішньої рефлексії та звернення до своїх внутрішніх ресурсів.'))
    special[message.from_user.id].append(await bot.send_message(message.from_user.id, '2. Сприйняття (S) vs Інтуїція (N): \nЛюди з орієнтацією на сприйняття більш схильні сприймати інформацію конкретно та фактично, тоді як ті, хто нахилені до інтуїції, більш схильні довіряти власним інтуїтивним сприйняттям та робити висновки на основі загальних концепцій.'))
    special[message.from_user.id].append(await bot.send_message(message.from_user.id, "3. Мислення (T) vs Відчуття (F): \nЛюди з орієнтацією на мислення приймають рішення, керуючись логікою та об'єктивністю, тоді як ті, хто нахилені до відчуття, надають перевагу емоційній або емпатичній оцінці ситуації."))
    special[message.from_user.id].append(await bot.send_message(message.from_user.id, "4. Судження (J) vs Пізнання (P): \nЛюди з орієнтацією на судження мають схильність до структурованості, організації та прийняття рішень, тоді як ті, хто нахилені до пізнання, відчувають більшу гнучкість у взятті рішень та відкриті до нових вражень."))
    special[message.from_user.id].append(await bot.send_message(message.from_user.id, 'Кожен з цих показників може мати дві протилежні характеристики, і комбінація чотирьох з них формує 16 можливих особистісних типів, таких як "ISTJ" (зосереджений на фактах та деталях, стійкий до змін), "ENFP" (креативний, енергійний та відкритий до нового), тощо. MBTI допомагає людям краще розуміти себе та інших, сприяє комунікації та спілкуванню у робочих та особистих взаємодіях.'))
    special[message.from_user.id].append(await bot.send_photo(message.from_user.id, photo='AgACAgIAAxkBAAIG1mXxr_yhoWNGtz5i8m2XdfOytN1tAAJP1zEbW5iQSwvjIxeuF_ntAQADAgADeAADNAQ', reply_markup=detail_mbti_keyboard()))
    time.sleep(1)
    await chat_text1[message.from_user.id].delete()



async def temperament(message: Message, bot: Bot):
    special[message.from_user.id] = []
    special[message.from_user.id].append(await bot.send_message(message.from_user.id, 'Темперамент - це психологічна характеристика особистості, яка визначається сукупністю стійких рис характеру, таких як емоційна стійкість, активність, суворість тощо. Він визначає, як людина реагує на різноманітні ситуації та взаємодіє з оточуючим середовищем.'))
    special[message.from_user.id].append(await bot.send_photo(message.from_user.id, photo='AgACAgIAAxkBAAIMKmXzBvTsYwF-fkXFNuMl5eAAAacuZAACNtkxG33gmEt8yPm-EBRuUgEAAwIAA3gAAzQE', reply_markup=temperament_keyboard()))

    time.sleep(1)
    await chat_text2[message.from_user.id].delete()


async def cunga(message: Message, bot: Bot):
    special[message.from_user.id] = []
    special[message.from_user.id].append(await bot.send_message(message.from_user.id, "Депресія - це психічний розлад, який характеризується постійним почуттям суму, втрати інтересу до різних аспектів життя, втратою енергії, зниженням самооцінки та іншими симптомами, які можуть впливати на психічне та фізичне здоров'я."))
    special[message.from_user.id].append(await bot.send_photo(message.from_user.id, photo='AgACAgIAAxkBAAIOXmXz654J4vOaIcvqF5knGqfGAYeHAAIw0zEbzRegS3bkTwlWpvl3AQADAgADeAADNAQ', reply_markup=cung_keyboard()))

    time.sleep(1)
    await chat_text2[message.from_user.id].delete()


