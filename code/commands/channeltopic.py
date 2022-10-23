@client.command()
@commands.has_permissions(manage_channels=True)
async def channeltopic(ctx, *, arg):
    channel = ctx.channel
    await channel.edit(topic = arg)
    embed = discord.Embed(colour = (clienthex),description = (f'{channel} topic set to {arg}'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
