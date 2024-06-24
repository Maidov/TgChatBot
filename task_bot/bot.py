import telebot
import requests
import tasks
from config import *
from weather import *

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
GISMETEO_API_URL = 'https://api.gismeteo.net/v2/weather/current/'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = (
        "Команды:\n"
        "/add <описание> - Добавить новую задачу\n"
        "/last10 - Получить список из 10 последних задач\n"
        "/today - Получить список всех задач за сегодня\n"
        "/done <задача> - Отметить задачу как выполненную\n"
        "/weather <город> - Узнать погоду на день через Gismeteo\n"
    )
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['add'])
def new_task(message):
    description = message.text[len('/add '):].strip()
    if description:
        tasks.add_task(message.from_user.id, description)
        bot.send_message(message.chat.id, "Задача добавлена.")
    else:
        bot.send_message(message.chat.id, "Введите описание задачи после команды /add.")

@bot.message_handler(commands=['last10'])
def last_tasks(message):
    last_tasks = tasks.get_last_tasks(message.from_user.id)
    if last_tasks:
        response = "Последние 10 задач:\n"
        for idx, task in enumerate(last_tasks):
            response += f"{idx + 1}. {task['description']} - {'Done' if task['done'] else 'Pending'} \n"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "У вас пока нет задач.")

@bot.message_handler(commands=['today'])
def today_tasks(message):
    today_tasks = tasks.get_today_tasks(message.from_user.id)
    if today_tasks:
        response = "Задачи на сегодня:\n"
        for idx, task in enumerate(today_tasks):
            response += f"{idx + 1}. {task['description']} - {'Done' if task['done'] else 'Pending'} \n"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "На сегодня задач нет.")

@bot.message_handler(commands=['done'])
def done_task(message):
    try:
        task_name = str(message.text[len('/done '):].strip()).lower()
        if tasks.mark_task_done(message.from_user.id, task_name):
            bot.send_message(message.chat.id, "Задача отмечена как выполненная.")
        else:
            bot.send_message(message.chat.id, "Не удалось найти задачу.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректную задачу.")

@bot.message_handler(commands=['weather'])
def send_weather(message):
    city = message.text[len('/weather '):].strip()
    if city:
        weather_info = get_weather(city)
        bot.reply_to(message, weather_info)
    else:
        bot.reply_to(message, "Введите название города после команды /weather.")

if __name__ == '__main__':
    bot.polling(none_stop=True)