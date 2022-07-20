import time
from telethon.sync import TelegramClient
from telethon import functions, types
import random

while 1>0:

    with TelegramClient('name',12816134, "3d6a556a840789d09ec6753b5cd7b7c7") as client:
        client.parse_mode = 'html'
        result = client(functions.messages.SendMessageRequest(
            peer='indiantradersonly',
            message='🔥 Tired of missing out on the signals? 🔥 \n\n ✅ Join the cheapest premium channel for crypto community with CORNIX bot  \n\n ✅ Check the plans and pay here: https://rigipay.com/g/1V0scZZVoG \n\n ✅ You will receive the premium link automatically to join. \n\n ✅ Message @adcode0 if you dont recieve link in 5 minutes after paying.',
            no_webpage=True
        ))

    time.sleep(7200)
