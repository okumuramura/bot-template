from typing import Optional, Callable, List, Dict

from bot.models.message import Answer, Message


Handler = Callable[[Message, List[str]], str]


class Bot:
    def __init__(self, name: str, prefix: str = '/') -> None:
        self.name = name
        self.prefix = prefix
        self.command_handlers: Dict[str, Handler] = {}

    def __default_unknown_command_handler(
            self,
            msg: str,
            args: List[str]
    ) -> str:
        return 'unknown command!'

    def all_commands(self) -> str:
        cmds = ""
        for command in self.command_handlers.keys():
            cmds += f"/{command}"
        cmds += "\r"
        return cmds

    def message(self, msg: Message) -> Optional[Answer]:
        if msg.text.startswith(self.prefix):
            text = msg.text[len(self.prefix):]
            command, *args = text.split()
            if command == "help":
                return Answer(self.all_commands())
            handler = self.command_handlers.get(
                command,
                self.__default_unknown_command_handler
            )
            try:
                answer = handler(msg, args)
            except Exception:
                return None

            return Answer(answer)
        return None

    def register_handler(self, command: str, handler: Handler) -> None:
        self.command_handlers[command] = handler

    def command(self, command: str):
        def decorator(f: Handler):
            self.register_handler(command, f)
            return f
        return decorator
