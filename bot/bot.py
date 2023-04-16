from typing import Optional, Callable, List, Dict
import colorama as cl
from bot.models.message import Answer, Message
from bot.models.command_help import CommandHelp
import bot.configuration as cnf

Handler = Callable[[Message, List[str]], str]


class Bot:
    def __init__(
            self,
            name: str = cnf.default_bot_name,
            prefix: str = cnf.default_bot_command_prefix,
            start_message: str = cnf.default_bot_start_message
    ) -> None:

        self.start_message = start_message
        self.name = name
        self.prefix = prefix
        self.command_handlers: Dict[str, Handler] = {}
        self.command_help: list[CommandHelp] = [
            CommandHelp('help', description="Выводит в чат все доступные команды", example_result="данное сообщение")
        ]

    def __default_unknown_command_handler(
            self,
            msg: str,
            args: List[str]
    ) -> str:
        return 'unknown command!'

    def all_commands(self) -> str:
        cmds = ""
        for command_help in self.command_help:
            cmds += f"{self.prefix}{command_help.command} "
            if command_help.args is not None:
                if len(command_help.args) == 0:
                    cmds += f"<{command_help.args[0]}>"
                else:
                    cmds += str(command_help.args).replace("'", "")
            cmds += f" | {command_help.description}"
            cmds += f" -> {command_help.example_result}"
            if command_help is not self.command_help[-1]:
                cmds += "\n"
        return cmds

    def message(self, msg: Message) -> Optional[Answer]:
        if msg.text.startswith(self.prefix):
            text = msg.text[len(self.prefix):]
            command, *args = text.split()
            if command == "help":
                return Answer(self.all_commands(), system=True)
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

    def register_command_help(self, command_help: CommandHelp)-> None:
        self.command_help.append(command_help)

    def command(
        self,
        command: str,
        args_name_list: list[str] or str or None = None,
        description: str or None = None,
        example_output: str or None = None
    ):
        def decorator(f: Handler):
            self.register_handler(command, f)
            self.register_command_help(
                CommandHelp(command, args_name_list, description, example_output)
            )
            return f

        return decorator
