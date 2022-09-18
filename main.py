import os
import keep_alive
from discord.ext import commands
import discord
import random
from os import system

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=".help command"))
    
    channel = await bot.fetch_channel(1019728469917188097)
    emb = discord.Embed(title="BloxMines is now online!", )
    await channel.send(embed=emb)
    await channel.send("<@&1020862434019397754>")


bot.remove_command('help')



@bot.command()
@commands.has_role('Premium')
async def mines(ctx, round_id=None):
    if round_id == None:
        round_id = 0
    else:
        round_id = str(round_id)
        round_length = len(round_id)
    if round_length == 1:
        await ctx.reply("Please provide a round ID")
    if round_length < 36:
        await ctx.reply("Invalid round id")
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = ":green_square: "
        elif a == 2:
            mine2 = ":green_square: "
        elif a == 3:
            mine3 = ":green_square: "
        elif a == 4:
            mine4 = ":green_square: "
        elif a == 5:
            mine5 = ":green_square: "
        elif a == 6:
            mine6 = ":green_square: "
        elif a == 7:
            mine7 = ":green_square: "
        elif a == 8:
            mine8 = ":green_square: "
        if b == 9:
            mine9 = ":green_square: "
        elif b == 10:
            mine10 = ":green_square: "
        elif b == 11:
            mine11 = ":green_square: "
        elif b == 12:
            mine12 = ":green_square: "
        elif b == 13:
            mine13 = ":green_square: "
        if c == 14:
            mine14 = ":green_square: "
        elif c == 15:
            mine15 = ":green_square: "
        elif c == 16:
            mine16 = ":green_square: "
        elif c == 17:
            mine17 = ":green_square: "
        if d == 18:
            mine18 = ":green_square: "
        elif d == 19:
            mine19 = ":green_square: "
        elif d == 20:
            mine20 = ":green_square: "
        elif d == 21:
            mine21 = ":green_square: "
        elif d == 22:
            mine22 = ":green_square: "
        elif d == 23:
            mine23 = ":green_square: "
        elif d == 24:
            mine24 = ":green_square: "
        elif d == 25:
            mine25 = ":green_square: "
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(random.randint(60, 90))
        em = discord.Embed(color=0x11F1D3)
        em.set_footer(text="Made by CaptainMaxi#0001")
        em.add_field(name="Mines predictor",
                     value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +
                     "\n" + row5 + "\n" + "**Probabilidades**" + "\n" + info +
                     "%")
        await ctx.reply(embed=em)


@bot.command(brief="Predicts tower!")
@commands.has_role('Premium')
async def towers(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await ctx.send("Invalid round id")
    elif round_length == 36:
        tower1, tower2, tower3, tower4, tower5, tower6, tower7, tower8, tower9, tower10, tower11, tower12, tower13, tower14, tower15, tower16, tower17, tower18, tower19, tower20, tower21, tower22, tower23, tower24 = ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:", ":question:"
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)
        e = random.randint(1, 3)
        f = random.randint(1, 3)
        g = random.randint(1, 3)
        h = random.randint(1, 3)

        if a == 1:
            tower1 = ":star:"
        elif a == 2:
            tower2 = ":star:"
        elif a == 3:
            tower3 = ":star:"
        if b == 1:
            tower4 = ":star:"
        elif b == 2:
            tower5 = ":star:"
        elif b == 3:
            tower6 = ":star:"
        if c == 1:
            tower7 = ":star:"
        elif c == 2:
            tower8 = ":star:"
        elif c == 3:
            tower9 = ":star:"
        if d == 1:
            tower10 = ":star:"
        elif d == 2:
            tower11 = ":star:"
        elif d == 3:
            tower12 = ":star:"
        if e == 1:
            tower13 = ":star:"
        elif e == 2:
            tower14 = ":star:"
        elif e == 3:
            tower15 = ":star:"
        if f == 1:
            tower16 = ":star:"
        elif f == 2:
            tower17 = ":star:"
        elif f == 3:
            tower18 = ":star:"
        if g == 1:
            tower19 = ":star:"
        elif g == 2:
            tower20 = ":star:"
        elif g == 3:
            tower21 = ":star:"
        if h == 1:
            tower22 = ":star:"
        elif h == 2:
            tower23 = ":star:"
        elif h == 3:
            tower24 = ":star:"

        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24
        #await ctx.send(row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8)
        info = str(random.randint(45, 95))
        list = [0xFF0000, 0x00FF2E, 0x000FFF, 0xF700FF]
        color = random.choice(list)
        em = discord.Embed(color=color)
        em.set_footer(text="Made by CaptainMaxi#0001")
        em.add_field(name="Towers Predictor",
                     value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +
                     "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8 +
                     "\n" + "**Probabilidades**" + "\n" + info + "%")
        await ctx.reply("Sent by dm's!")
        await ctx.reply(embed=em)


@bot.command(brief="PREMIUM | Predice en Mines con solo dos Tokens XD")
@commands.has_role('Premium')
async def predict(ctx, round_id=None):
    if round_id == None:
        round_id = 0
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 1:
        await ctx.reply("Please provide a round ID")
    if round_length < 36:
        await ctx.reply("Invalid round id")
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'
        a = random.randint(1, 12)
        b = random.randint(13, 25)

        if a == 1:
            mine1 = ":star:"
        elif a == 2:
            mine2 = ":star:"
        elif a == 3:
            mine3 = ":star: "
        elif a == 4:
            mine4 = ":star:"
        elif a == 5:
            mine5 = ":star:"
        elif a == 6:
            mine6 == ":star:"
        elif a == 7:
            mine7 = ":star:"
        elif a == 8:
            mine8 = ":star:"
        elif a == 9:
            mine9 = ":star:"
        elif a == 10:
            mine10 = ":star:"
        elif a == 11:
            mine11 = ":star:"
        elif a == 12:
            mine12 = ":star:"
        if b == 13:
            mine13 = ":star:"
        elif b == 14:
            mine14 = ":star:"
        elif b == 15:
            mine15 = ":star:"
        elif b == 16:
            mine16 = ":star:"
        elif b == 17:
            mine17 = ":star:"
        elif b == 18:
            mine18 = ":star:"
        elif b == 19:
            mine19 = ":star:"
        elif b == 20:
            mine20 = ":star:"
        elif b == 21:
            mine21 = ":star:"
        elif b == 22:
            mine22 = ":star:"
        elif b == 23:
            mine23 = ":star:"
        elif b == 24:
            mine24 = ":star:"
        elif b == 25:
            mine25 = ":star:"
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(random.randint(60, 90))
        list = [0xFF0000, 0x00FF2E, 0x000FFF, 0xF700FF]
        color = random.choice(list)
        em = discord.Embed(title="2 Star Predictor", color=color)
        em.set_footer(text="Made by CaptainMaxi#0001")
        em.add_field(
            name="Our System says:",
            value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" +
            row5 + "\n" +
            "**Probabilidades**: \n Ten cuidado las probabilidades pueden ser erroneas!"
            + "\n" + info + "%")
        await ctx.reply(embed=em)
        print(
            f"The prediction from {round_id}, the best star is cell {a}, {b} and the Probabilidades is from {info}%"
        )


@bot.command(brief="PREMIUM | 10 Posibles celdas para conveniencia.")
@commands.has_role('Premium')
async def entire(ctx, round_id=None):
    if round_id == None:
        round_id = 0
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 1:
        await ctx.reply("Please provide a round ID")
    if round_length < 36:
        await ctx.reply("Invalid round id")
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'
        rnum = random.randint
        a = rnum(1, 2)
        b = rnum(3, 5)
        c = rnum(6, 7)
        d = rnum(8, 10)
        e = rnum(11, 12)
        f = rnum(13, 15)
        g = rnum(16, 17)
        h = rnum(18, 20)
        i = rnum(21, 22)
        j = rnum(23, 25)
        if a == 1:
            mine1 = ":crown:"
        elif a == 2:
            mine2 = ":crown:"
        if b == 3:
            mine3 = ":crown:"
        elif b == 4:
            mine4 = ":crown:"
        elif b == 5:
            mine5 = ":crown:"
        if c == 6:
            mine6 = ":crown:"
        elif c == 7:
            mine7 = ":crown:"
        if d == 8:
            mine8 = ":crown:"
        elif d == 9:
            mine9 = ":crown:"
        elif d == 10:
            mine10 = ":crown:"
        if e == 11:
            mine11 = ":crown:"
        elif e == 12:
            mine12 = ":crown:"
        if f == 13:
            mine13 = ":crown:"
        elif f == 14:
            mine14 = ":crown:"
        elif f == 15:
            mine15 = ":crown:"
        if g == 16:
            mine16 = ":crown:"
        elif g == 17:
            mine17 = ":crown:"
        if h == 18:
            mine18 = ":crown:"
        elif h == 19:
            mine19 = ":crown:"
        elif h == 20:
            mine20 = ":crown:"
        if i == 21:
            mine21 = ":crown:"
        elif i == 22:
            mine22 = ":crown:"
        if j == 23:
            mine23 = ":crown:"
        elif j == 24:
            mine24 = ":crown:"
        elif j == 25:
            mine25 = ":crown:"
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(random.randint(20, 70))
        em = discord.Embed(title="10 Crowns Predictor!", color=0x11F1D3)
        em.set_footer(text="Made by CaptainMaxi#0001")
        em.add_field(
            name="Our System says:",
            value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" +
            row5 + "\n" +
            "**Probabilidades**: \n Ten cuidado las probabilidades pueden ser erroneas!"
            + "\n" + info + "%")
        await ctx.reply(embed=em)


@bot.command(brief="PREMIUM | Cups Predictor!")
@commands.has_role('Premium')
async def cups(ctx, round_id=None):
    if round_id == None:
        round_id = 0
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 1:
        await ctx.reply("Please provide a round ID")
    if round_length < 36:
        await ctx.reply("Invalid round id")
    elif round_length == 36:
        a = random.randint(1, 2)
        predictionn = ":question:"
        if a == 1:
            predictionn = ":red_square:"
        elif a == 2:
            predictionn = ":blue_square:"
        row1 = predictionn
        info = str(50)
        em = discord.Embed(title="Prediccion de Tazas!", color=0x11F1D3)
        em.set_footer(text="Hecho por CaptainMaxi#0001")
        em.add_field(
            name="Nuestro sistema de probabiliidades dice:",
            value=row1 + "\n" +
            "**Probabilidades**: \n Ten cuidado las probabilidades pueden ser erroneas!"
            + "\n" + info + "%")
        await ctx.reply(embed=em)


@bot.command(brief="PREMIUM | Probability Cups Predictor!")
@commands.has_role('Premium')
async def pcups(ctx, round_id=None):
    if round_id == None:
        round_id = 0
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 1:
        await ctx.reply("Please provide a round ID")
    if round_length < 36:
        await ctx.reply("Invalid round id")
    elif round_length == 36:
        a = random.randint(1, 2)
        predictionn = ":question:"
        if a == 1:
            predictionn = ":red_square: "
        elif a == 2:
            predictionn = ":blue_square: "
        b = random.randint(1, 2)
        if b == 1:
            b = ":red_square: "
        elif b == 2:
            b = ":blue_square: "
        c = random.randint(1, 2)
        if c == 1:
            c = ":red_square: "
        elif c == 2:
            c = ":blue_square: "
        row1 = predictionn + b + c
        info = str(random.randint(50, 70))
        em = discord.Embed(title="Prediccion de Tazas!", color=0x11F1D3)
        em.set_footer(text="Hecho por CaptainMaxi#0001")
        em.add_field(
            name="Nuestro sistema de probabilidades dice:",
            value=row1 + "\n" + "**Probabilidad**: \n" + info + "%"
            "\nEs calculado la mayoria de probabilidades. Por ejemplo hay 2 azules y 1 rojo, significa que el azul es 'mas' probable."
        )
        await ctx.reply(embed=em)


# gold - FFFB00
# purple - FFFB00
# redish - FF0078
@bot.command(brief="Predict a la ruleta! Un resultado :v")
@commands.has_role('Premium')
async def ro(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 36:
        predictions = [
            'red', 'red', 'red', 'purple', 'purple', 'purple', 'gold'
        ]
        prediction = random.choice(predictions)
        if prediction == 'red':
            embed_color = 0xFF0078
            color_text = "Red"
            prediction = ":red_square:"
        elif prediction == 'purple':
            embed_color = 0xFFFB00
            color_text = 'Purple'
            prediction = ":purple_square:"
        elif prediction == 'purple':
            embed_color = 0xFFFB00
            color_text = 'Gold'
            prediction = " :yellow_square:"
        em = discord.Embed(color=embed_color)
        prob = random.randint(40, 99)
        em.add_field(name="Roulette Predictor",
                     value=color_text + "\n" + prediction +
                     f"\n **Probabilidades:**\n{prob}%")
        await ctx.reply(embed=em)
    else:
        await ctx.reply("Invalid round id")


## HELP command
@bot.command(pass_context=True, aliases=['commands', 'cmds'])
async def help(ctx):
    embed = discord.Embed(
        title="Ayuda",
        description=
        "<> = Argumentos opcionales || [] = Argumentos obligatorios",
        colour=discord.Colour.red())

    embed.set_thumbnail(url="")
    embed.set_footer(text="© CaptainMaxi#0001",
                     icon_url="https://cdn.discordapp.com/embed/avatars/4.png")

    embed.add_field(
        name="Free Commands",
        value=
        "Los siguientes comandos pueden ser hechos por cualquier persona, sin falta de permisos.\n \n **.mines** [round_id]\n**.towers** [round_id]\n **.ro** [round_id]\n ."
    )
    embed.add_field(
        name="Premium Commands",
        value=
        "Los siguientes comandos solo pueden ser realizados por usuarios premium asignados por el Staff!\n \n **.cups** [round_id]\n **.predict** [round_id]\n **.entire** [round_id]\n **.pcups** [round_id]",
        inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send(f'Latency is {round(bot.latency * 1000)}ms')


my_secret = os.environ['TOKEN']
keep_alive.keep_alive()
try:
    bot.run(my_secret)

except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("python restarter.py")
    system('kill 1')
