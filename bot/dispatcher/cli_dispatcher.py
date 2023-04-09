import os

from bot.bot import Bot
from bot.models.message import Message


def cli_output(text: str, *args, **kwargs) -> None:
    print(text, *args, **kwargs)


class CliDispatcher:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.message_id = 0

    def start_polling(self) -> None:
        cli_output(f'\nHi, i am bot {self.bot.name}, write /help to get all my commands')
        try:
            self.__loop()
        except KeyboardInterrupt:
            cli_output('bye :)')

    def __loop(self) -> None:
        while True:
            line = input('User > | ')
            answer = self.msg_handler(line)
            return answer

    def msg_handler(self, line: str):
        msg = Message(
            id=self.message_id,
            text=line,
            author=os.getlogin()
        )
        answer = self.bot.message(msg)
        if answer is not None:
            cli_output(f'{self.bot.name} |', answer.text)
        return answer
