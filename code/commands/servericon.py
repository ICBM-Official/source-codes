@client.command()
async def servericon(ctx):
    embed = discord.Embed(colour = (clienthex),title = ('Servericon'), timestamp = (ctx.message.created_at))
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon.url)
    embed.set_image(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)
    await ctx.message.delete()
