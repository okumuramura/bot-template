from typing import List

from bot.bot import Bot
from bot.models.message import Message
from bot.dispatcher.cli_dispatcher import CliDispatcher


bot = Bot('my-bot')
dispatcher = CliDispatcher(bot)


@bot.command('hello')
def hello_handler(msg: Message, args: List[str]) -> str:
    return f'Hello, {msg.author}!'

@bot.command('Case', ignore_case=False)
def case_handler(msg: Message, args: List[str]) -> str:
    return 'This command is casesensetive!'


# bot.register_handler('hello', hello_handler)

if __name__ == '__main__':
    dispatcher.start_polling()
