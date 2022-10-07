#* Timer
import logging
import datetime
import asyncio
from time import sleep

#* Discord
import discord
from discord import Message

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f"Sesion iniciada como {client.user}")

message_count: list[str] = []
timer = 12 * 3600


@client.event
async def on_message(message: Message):

    if message.author == client.user:
        return

    if message.channel.id == 1017483825678397471:
        message_count.append(message.content)
        print(message.channel.id)
        print(message_count)

    if len(message_count) == 11:
        await message.channel.send("Prohibido mandar mas mensajes. PARA AHORA MISMO O SERAS FUSILADO!")
        global timer
        while timer != 0:
            timer = timer - 1
            await asyncio.sleep(1)
            print(timer, end="\r")
        if timer == 0:
            timer = 12 * 3600
            message_count.clear()
    if len(message_count) > 11 and message.channel.id == 1017483825678397471:
        await message.channel.send(f"Aun quedan {datetime.timedelta(hours = timer / 3600)} horas para que el sol vuelva a salir por ESPAÑA")
        await message.delete(delay=1/100000)
