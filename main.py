from typing import List
from random import choice

from bot.bot import Bot
from bot.models.message import Message
from bot.dispatcher.cli_dispatcher import CliDispatcher


bot = Bot('my-bot')
dispatcher = CliDispatcher(bot)


@bot.command('hello')
def hello_handler(msg: Message, args: List[str]) -> str:
    return f'Hello, {msg.author}!'


@bot.command('coin')
def random_coin_handler(msg: Message, args: List[str]) -> str:
    return f"{choice(['орел', 'решка'])}"

@bot.command('throw')
def throw_smth_handler(msg: Message, args: List[str]) -> str:
    if args:
        return f"{msg.author} кинул {args[0]}"
    return f"{msg.author} кинул снежок"

@bot.command('kiss')
def kiss_handler(msg: Message, args: List[str]) -> str:
    return f"{msg.author} поцеловал {args[0]}"

# bot.register_handler('hello', hello_handler)

if __name__ == '__main__':
    dispatcher.start_polling()
