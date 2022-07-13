import discord as ds

client = ds.Client()

@client.event
async def on_connect():
    print("Tito franco conectado, ARRIBA!")

@client.event
async def on_ready():
    print("Nos hemos logueado como {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$españa"):
        await message.channel.send("ARRIBA!")
    
    if message.content.startswith("$los moros?"):
        await message.channel.send("FUERA!")
    
    if message.content.startswith("$los sudacas?"):
        await message.channel.send("FUERA!\nFUERA QUIEN SE SALGA DE LA FRONTERAS DE MI BANDERA")

    if message.content.startswith("$cara a donde?"):
        await message.channel.send("""Cara al sol con la camisa nueva
            Que tú bordaste en rojo ayer,
            Me hallará la muerte si me lleva
            Y no te vuelvo a ver.""")
    
    if message.content.startswith("$cuanto es 1 + 1?"):
        await message.channel.send("estas fusilado")

@client.event
async def on_disconnect():
    print("Hasta pronto, cuiden España por mi")