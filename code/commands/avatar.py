@client.command()
async def avatar(ctx, member : discord.Member = None):
    member = ctx.message.author if not member else member
    embed = discord.Embed(colour=member.color, title='Avatar', timestamp = (ctx.message.created_at))
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)
    await ctx.message.delete()
