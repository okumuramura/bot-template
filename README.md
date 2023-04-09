# Шаблон универсального бота
> Для образовательных целей, в реальных проектах не используйте

### Запуск
```bash
python main.py
```

### Как использовать
```python
from bot.bot import Bot
from bot.dispatcher import CliDispatcher
from bot.models.message import Message

bot = Bot('my-bot')
dispatcher = CliDispatcher(bot=bot)

@bot.command('help')
def help_handler(msg: Message) -> str:
    return 'вот так нужно пользоваться моим ботом'

if __name__ == '__main__':
    dispatcher.start_polling()
```

### Варианты

| команда | действие | пример |
| - | - | - |
| /time | вывести текущее время UTC | /time<br>11:12
| /coin | вывести случайно "орёл" или "решка" | /coin<br>орёл |
| /throw `[what]`| вывести сообщение, что автор кинул что-то. Если не указано что, то кидаем снежок | /throw копьё<br>Вася кинул копьё |
| /kiss `<who>` | вывести сообщение, что пользователь поцеловал кого-то. Если не указано, кого, то ничего не выводить | /kiss Машу<br>Кирилл поцеловал Машу |
| /calc `<a>` `<op>` `<b>` | вывести результат математической операции. Допустимые `op`: '+', '-', '*', '/'| /calc 5 / 0<br>на ноль делить нельзя!|