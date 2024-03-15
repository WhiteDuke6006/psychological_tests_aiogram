from aiogram import Bot, Dispatcher
from core.middlewares.settings import settings
from core.psychological_tests.CUNGA import start_cung, true_cung, false_cung, get_cung_result
from core.handlers.basic import start_message, tests, mbti, temporarily_unavailable, detail_mbti, temperament, cunga
from core.psychological_tests.MBTI import start_mbti_test, get100true, get50true, get25true, none, get25false, get50false, get100false, get_mbti_result
from core.psychological_tests.TEMPERAMENT import start_temperament, true, false, get_temperament_result
from aiogram.filters import Command
from aiogram import F
import asyncio


async def start():
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.message.register(start_message, Command(commands='start'))
    dp.callback_query.register(tests, F.data == 'all_tests')
    dp.callback_query.register(start_message, F.data == 'back')
    dp.callback_query.register(mbti, F.data == 'mbti')
    dp.callback_query.register(temporarily_unavailable, F.data == 'rockich')
    dp.callback_query.register(tests, F.data == 'exit')
    dp.callback_query.register(detail_mbti, F.data == 'detail_mbti')
    dp.callback_query.register(start_mbti_test, F.data == 'start_mbti')
    dp.callback_query.register(get100true, F.data == '100true')
    dp.callback_query.register(get50true, F.data == '50true')
    dp.callback_query.register(get25true, F.data == '25true')
    dp.callback_query.register(none, F.data == 'none')
    dp.callback_query.register(get25false, F.data == '25false')
    dp.callback_query.register(get50false, F.data == '50false')
    dp.callback_query.register(get100false, F.data == '100false')
    dp.callback_query.register(get_mbti_result, F.data == 'to_result_mbti')
    dp.callback_query.register(temperament, F.data == 'temperament')
    dp.callback_query.register(start_temperament, F.data == 'start_temperament')
    dp.callback_query.register(true, F.data == 'true')
    dp.callback_query.register(false, F.data == 'false')
    dp.callback_query.register(get_temperament_result, F.data == 'to_result_temperament')
    dp.callback_query.register(cunga, F.data == 'cung')
    dp.callback_query.register(start_cung, F.data == 'start_cung')
    dp.callback_query.register(true_cung, F.data == 'true_cung')
    dp.callback_query.register(false_cung, F.data == 'false_cung')
    dp.callback_query.register(get_cung_result, F.data == 'to_result_cung')



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())



