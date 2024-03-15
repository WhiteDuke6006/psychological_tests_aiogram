from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot

async def set_commands(bot:Bot):
    commands = [
        BotCommand(command='start',
                   description='початок роботи')
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
