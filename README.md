# TaskBot
### TaskBot - это Telegram-бот для управления задачами и получения прогноза погоды. Бот поддерживает следующие функции:

- Добавление новой задачи
- Получение списка из 10 последних задач
- Получение списка всех задач за сегодня
- Отметка задачи как выполненной
- Получение прогноза погоды через API

## Установка
#### Клонируйте репозиторий:
```sh
git clone https://github.com/yourusername/TaskBot.git
cd TaskBot
```
#### Установите зависимости:
```sh
pip install -r requirements.txt
```
#### Настройка
- Создайте бота в Telegram и получите API токен.
- Создайте файл config.py и добавьте ваш API токен:
```python
# в файле config.py
# Telegram Bot Token
TELEGRAM_BOT_TOKEN = '>>>YOUR TOKEN HERE<<<'
```
#### Запуск
```sh
python bot.py
```
#### Команды
- /start или /help - Отобразить справку по доступным командам.
- /add <описание> - Добавить новую задачу.
- /last10 - Получить список из 10 последних задач.
- /today - Получить список всех задач за сегодня.
- /done <задача> - Отметить задачу как выполненную.
- /weather <город> - Узнать погоду на день через Gismeteo.
#### Структура проекта
- bot.py - Основной файл бота, содержит описание команд и логику взаимодействия.
- tasks.py - Функции для работы с задачами (добавление, получение, отметка как выполненная).
- requirements.txt - Зависимости проекта.
- weather.py - Работа с API погоды
