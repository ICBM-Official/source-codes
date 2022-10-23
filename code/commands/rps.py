@client.command()
@commands.cooldown(1,10, commands.BucketType.user)
async def rps(ctx):
    await ctx.message.delete()
    rpsGame = ['rock', 'paper', 'scissors']
    images = ['https://cdn.discordapp.com/attachments/933743205810327572/972944621409808484/scissors.jpg', 'https://cdn.discordapp.com/attachments/933743205810327572/972944621665665164/paper.jpg','https://cdn.discordapp.com/attachments/933743205810327572/972944621862785035/rock.jpg']
    tie = "https://cdn.discordapp.com/attachments/929127439832084570/972961018064039946/naples-yellow-painted-swatch.jpg"
    win = "https://cdn.discordapp.com/attachments/929127439832084570/972961018340843620/Solid_green.svg.png"
    loss = "https://cdn.discordapp.com/attachments/929127439832084570/972961017711689748/download.png"
    comp_choice = random.choice(rpsGame)
    img = random.choice(images)
    rock = "<:rock:972946391913594951>"
    paper = "<:paper:972946391871660072>"
    scissors = "<:scissors:972946391636799540>"
    embed = discord.Embed(colour = (clienthex),title = ('Rock Paper Scissors'),description = (f"""Choose wisely
{rock} - Rock
{paper} - Paper
{scissors} - Scissors"""), timestamp = (ctx.message.created_at))
    embed.set_thumbnail(url=img)
    embed.set_footer(text=f"{ctx.message.author}")
    message = await ctx.send(embed=embed)
    await message.add_reaction(rock)
    await message.add_reaction(paper)
    await message.add_reaction(scissors)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in [rock, paper, scissors]

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=10, check=check)
            if str(reaction.emoji) == rock:
                if comp_choice == 'rock':
                    newembed = discord.Embed(colour = (clienthex),title = ('You tied'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=tie)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
                elif comp_choice == 'paper':
                    newembed = discord.Embed(colour = (clienthex),title = ('You lost'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=loss)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
                elif comp_choice == 'scissors':
                    newembed = discord.Embed(colour = (clienthex),title = ('You won!'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=win)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
            elif str(reaction.emoji) == paper:
                if comp_choice == 'rock':
                    newembed = discord.Embed(colour = (clienthex),title = ('You won'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=win)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
                elif comp_choice == 'paper':
                    newembed = discord.Embed(colour = (clienthex),title = ('You tied'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=tie)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
                elif comp_choice == 'scissors':
                    newembed = discord.Embed(colour = (clienthex),title = ('You lost'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=loss)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
            elif str(reaction.emoji) == scissors:
                if comp_choice == 'rock':
                    newembed = discord.Embed(colour = (clienthex),title = ('You lost'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=loss)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
                elif comp_choice == 'paper':
                    newembed = discord.Embed(colour = (clienthex),title = ('You won!'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=win)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
                elif comp_choice == 'scissors':
                    newembed = discord.Embed(colour = (clienthex),title = ('You tied'),description = (f"""The bot chose {comp_choice}"""))
                    newembed.set_thumbnail(url=tie)
                    newembed.set_footer(text=f"{ctx.message.author}")
                    await message.edit(embed=newembed)
                    await message.remove_reaction(reaction, user)
                    await message.remove_reaction(rock, client.user)
                    await message.remove_reaction(paper, client.user)
                    await message.remove_reaction(scissors, client.user)
            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            break
