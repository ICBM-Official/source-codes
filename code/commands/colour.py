@client.command()
async def colour(ctx, value : str):
    embed = discord.Embed(colour=clienthex, title='Colour', timestamp = (ctx.message.created_at))
    embed.set_thumbnail(url='http://www.colorhexa.com/{}.png'.format(str(value).strip("#")))
    embed.set_image(url='http://www.colorhexa.com/{}.png'.format(str(value).strip("#")))
    await ctx.send(embed=embed)
