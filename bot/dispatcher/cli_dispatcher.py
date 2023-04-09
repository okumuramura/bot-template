import os

from bot.bot import Bot
from bot.models.message import Message


class CliDispatcher:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.message_id = 0

    def start_polling(self) -> None:
        try:
            self.__loop()
        except KeyboardInterrupt:
            print('bye :)')

    def __loop(self) -> None:
        while True:
            line = input('> ')
            msg = Message(
                id=self.message_id,
                text=line,
                author=os.getlogin()
            )
            answer = self.bot.message(msg)
            if answer is not None:
                print('<', answer.text)
