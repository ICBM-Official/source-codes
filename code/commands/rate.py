@client.command()
async def rate(ctx, * , arg):
    number = random.randint(0,10)
    end = 11 - number
    bar = ''

    for i in range(0, number):
        bar = bar + '⭐'
    emoji = '<:grey_star:909179980758532116>'
    for i in range(1, end):
        bar = bar + emoji
    embed =  discord.Embed(colour=clienthex, title=f'I rate __{arg}__ {number} stars out of 10', timestamp=ctx.message.created_at, description=bar)
    await ctx.send(embed=embed)
