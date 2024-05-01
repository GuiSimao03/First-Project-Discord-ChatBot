import discord
import asyncio
from time import sleep
from random import choice

## importando o bot ao discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

## chamando o bot no canal
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    ## conversa com o bot
    if message.content.startswith('game1'):
        await message.channel.send('Cara ou Coroa?')

        ## Espera a resposta do usuário
        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            user_choice = await client.wait_for('message', check=check, timeout=30)
            if user_choice.content.lower() == 'cara' or user_choice.content.lower() == 'coroa':
                ## Resultado aleatório
                options = ['cara', 'coroa']
                result = choice(options)
                await message.channel.send(f'O resultado foi: {result}')
                sleep(1)
                if user_choice.content.lower() == result:
                    await message.channel.send('Você acertou!!!')
                else:
                    await message.channel.send("Você errou!!!")
            else:
                await message.channel.send('Escolha inválida. Por favor, digite "cara" ou "coroa".')
        except asyncio.TimeoutError:
            await message.channel.send('Tempo esgotado. Você demorou muito para escolher.')

    if message.content.startswith('game2'):
        await message.channel.send('Pedra, Papel ou Tesoura?')

        def check(m):
            return m.author == message.author and m.channel == message.channel
        
        try:
            user_choice = await client.wait_for('message', check=check, timeout=30)
            if user_choice.content.lower() == 'pedra' or user_choice.content.lower() == 'papel' or user_choice.content.lower() == 'tesoura':
                ## Resultado aleatório
                options = ['pedra', 'papel', 'tesoura']
                result = choice(options)
                await message.channel.send(f'O resultado foi: {result}')
                sleep(1)
                if user_choice.content.lower() == result:
                    await message.channel.send('Você Empatou!!!')
                else:
                    if (user_choice.content.lower() == 'pedra' and result == 'tesoura') or (user_choice.content.lower() == 'papel' and result == 'pedra') or (user_choice.content.lower() == 'tesoura' and result == 'papel'):
                        await message.channel.send('Você Ganhou!!!')
                    else:
                        await message.channel.send('Você Perdeu!!!')
            else:
                await message.channel.send('Escolha inválida. Por favor, digite "pedra" , "papel" ou "tesoura".')
        except asyncio.TimeoutError:
            await message.channel.send('Tempo esgotado. Você demorou muito para escolher.')
        

client.run('YOUR BOT TOKEN')
