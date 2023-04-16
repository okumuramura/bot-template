from typing import List
from bot.bot import Bot
from bot.models.message import Message
from bot.dispatcher.cli_dispatcher import CliDispatcher
from bot.dispatcher.vk_despatcher import VkDispatcher

vk_api_token = '''vk1.a.URgckFWnoKOkZAN1qX_QifHRC_g5xLT0M3gO0-CH4RH4D-BP-PokvRYi9pJgRN21xqBfgOo09
-Vs_mEbhXJpislkKDnkSRwtKgDAiwbm1Z5aqYstkJtItfpWnDUufzpGFMUl_13mclCOjvI4M4Oce5k8RV1FYV8VDyW8
-_y5My3JwSxv7w9xWvt7D3RTxXffhR6GvqddfKqtg2W-SsHVOg'''

bot = Bot('my-bot')
dispatcher = CliDispatcher(bot)
vk_dispatcher = VkDispatcher(bot, vk_api_token)


@bot.command('hello', description="Выводит в чат приветствие пользователя", example_output="Hello, {Username}")
def hello_handler(msg: Message, args: List[str]) -> str:
    return f'Hello, {msg.author}!'


@bot.command('sum', args_name_list=["<a>", "<b>"], description="Выводит в чат сумму двух чисел", example_output="2 + 3 = 5")
def hello_handler(msg: Message, args: List[str]) -> str:
    return f'{float(args[0])} + {float(args[1])} = {float(args[0]) + float(args[1])}'


if __name__ == '__main__':
    vk_dispatcher.vk_start_pooling()
