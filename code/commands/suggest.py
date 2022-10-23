@client.command(pass_context=True)
@commands.cooldown(1,21600, commands.BucketType.user)
async def suggest(ctx, *, arg):
    channel = discord.utils.get(ctx.message.guild.channels, name='suggestions')
    if channel == None:
        c = await ctx.message.guild.create_text_channel(name=f'suggestions', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        channel = discord.utils.get(ctx.message.guild.channels, name='suggestions')
    embed = discord.Embed(
        colour = discord.Colour(clienthex),
        timestamp = (ctx.message.created_at),
    )
    embed.set_author(name=ctx.message.author)
    embed.add_field(name='Suggestion', value=arg, inline=False)
    m = await channel.send(ctx.message.author.mention)
    m = await channel.send(embed=embed)
    m = await ctx.send(f"Suggestion sent")
    await ctx.message.delete()
