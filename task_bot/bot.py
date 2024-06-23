import telebot
from config import TELEGRAM_BOT_TOKEN
from tasks import add_task, get_last_10_tasks, get_tasks_for_today, mark_task_as_completed
from weather import get_weather

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

#TODO: Переделать логику отображения/завершения задач
# пользователь должен понимать какую задачу он выполняет
# Либо нужно чтобы в любом списке были глобальные номера задач
# Либо как-то ебаться с локальными

#TODO: Переписать на русский фразы

#TODO: Сделать функционал /help

#TODO: Добавить кнопки
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Task Bot! You can manage your tasks and get weather updates.")

@bot.message_handler(commands=['add'])
def add_new_task(message):
    task_text = message.text[len('/add '):].strip()
    if task_text:
        add_task(task_text)
        bot.reply_to(message, "Task added successfully.")
    else:
        bot.reply_to(message, "Please provide the task description after the command.")

@bot.message_handler(commands=['last10'])
def send_last_10_tasks(message):
    tasks = get_last_10_tasks()
    if tasks:
        response = "\n".join([f"{i + 1}. {task['text']} - {'Completed' if task['completed'] else 'Pending'}" for i, task in enumerate(tasks)])
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "No tasks found.")

@bot.message_handler(commands=['today'])
def send_today_tasks(message):
    tasks = get_tasks_for_today()
    if tasks:
        response = "\n".join([f"{i + 1}. {task['text']} - {'Completed' if task['completed'] else 'Pending'}" for i, task in enumerate(tasks)])
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "No tasks found for today.")

@bot.message_handler(commands=['complete'])
def complete_task(message):
    try:
        task_index = int(message.text[len('/complete '):].strip()) - 1
        task = mark_task_as_completed(task_index)
        if task:
            bot.reply_to(message, "Task marked as completed.")
        else:
            bot.reply_to(message, "Task not found.")
    except ValueError:
        bot.reply_to(message, "Please provide a valid task number.")

@bot.message_handler(commands=['weather'])
def send_weather(message):
    city = message.text[len('/weather '):].strip()
    if city:
        weather_info = get_weather(city)
        bot.reply_to(message, weather_info)
    else:
        bot.reply_to(message, "Please provide the city name after the command.")

bot.polling()