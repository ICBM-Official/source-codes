@client.command()
@commands.has_permissions(manage_channels=True)
async def channelname(ctx, *, arg):
    channel = ctx.channel
    await channel.edit(name = arg)
    embed = discord.Embed(colour = (clienthex),description = (f'{channel} name set to {arg}'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
