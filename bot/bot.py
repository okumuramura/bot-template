from typing import Optional, Callable, List, Dict

from bot.models.message import Message, Answer


Handler = Callable[[Message, List[str]], str]


class Bot:
    def __init__(self, name: str, prefix: str = '/') -> None:
        self.name = name
        self.prefix = prefix
        self.command_handlers: Dict[str, Handler] = {}
        self.command_parameters: Dict[str, Dict()] = {}

    def __default_unknown_command_handler(
            self,
            msg: str,
            args: List[str]
    ) -> str:
        return 'unknown command!'

    def message(self, msg: Message) -> Optional[Answer]:
        if msg.text.startswith(self.prefix):
            text = msg.text[len(self.prefix):]
            command, *args = text.split()

            if parameters := self.command_parameters.get( command.lower(), None ):  # Проверка если комманда не проверяет заглавные буквы
                if parameters['ignoreCase']:
                    command = command.lower()

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

    def register_handler(self, command: str, handler: Handler, ignoreCase: bool = True) -> None:
        if not ignoreCase: command = command.lower()
        self.command_handlers[command] = handler
        self.command_parameters[command] = {
            'ignoreCase': ignoreCase
        }

    def command(self, command: str, ignoreCase: bool = True):
        def decorator(f: Handler):
            self.register_handler(command, f, ignoreCase = ignoreCase)
            return f
        return decorator
