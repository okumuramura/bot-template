from typing import List
from bot.bot import Bot
from bot.models.message import Message
from bot.dispatcher.cli_dispatcher import CliDispatcher


bot = Bot('my-bot')
dispatcher = CliDispatcher(bot)


@bot.command('hello', description="Выводит в чат приветствие пользователя", example_output="Hello, {Username}")
def hello_handler(msg: Message, args: List[str]) -> str:
    return f'Hello, {msg.author}!'


@bot.command('sum', args_name_list=["<a>", "<b>"], description="Выводит в чат сумму двух чисел", example_output="2 + 3 = 5")
def hello_handler(msg: Message, args: List[str]) -> str:
    return f'{float(args[0])} + {float(args[1])} = {float(args[0]) + float(args[1])}'


if __name__ == '__main__':
    dispatcher.start_polling()
