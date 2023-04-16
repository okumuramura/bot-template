import vk_api
import time
from vk_api.longpoll import VkLongPoll, VkEventType

from bot.bot import Bot
from bot.models.message import Message as Bot_Message


class VkDispatcher:
    def __init__(self, _bot: Bot, token: str):
        self.powered = False
        self.bot = _bot
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkLongPoll(self.vk)

    def vk_start_pooling(self):
        print("vk_despatcher started")
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    self.msg_handler(event.user_id, event.text)

    def msg_handler(self, id: int, msg: str):
        answer = self.bot.message(Bot_Message(id=id, text=msg))
        if answer is not None:
            self.write_msg(id, answer.text)

    def write_msg(self, user_id: int, message: str) -> None:
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0})
