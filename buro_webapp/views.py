from django.shortcuts import render
from aiogram import Bot, types
import asyncio
bot = Bot(token='7083425620:AAHaBufx9L-fcgAQ2ij7eGnyt2UyF4ArCLw')
loop = asyncio.get_event_loop()

async def send_message_to_telegram(chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        chat_id = '-1002091116164'
        message = f"Имя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        
        loop.run_until_complete(send_message_to_telegram(chat_id, message))
        
    return render(request, 'buro_webapp/index.html')

def privacy(request):
    return render(request, 'buro_webapp/privacy.html')