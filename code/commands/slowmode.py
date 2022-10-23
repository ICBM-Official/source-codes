@client.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, channel : discord.TextChannel, num : int):
    await channel.edit(slowmode_delay = num)
    embed = discord.Embed(colour = (clienthex),description = (f'{channel} slowmode set to {num}'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
