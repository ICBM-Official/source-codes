@client.command(pass_context=True , aliases=['cc'])
@commands.has_permissions(manage_channels=True)
async def createchannel(ctx, type : str, *, arg):
    await ctx.message.delete()
    if type == 'text':
        embed = discord.Embed(colour = (clienthex),title = ('Text'),description = (f'Channel made'), timestamp = (ctx.message.created_at))
        await ctx.send(embed=embed)
        await ctx.message.guild.create_text_channel(name=arg, category=ctx.message.channel.category)
    elif type == 'voice':
        embed = discord.Embed(colour = (clienthex),title = ('Voice'),description = (f'Channel made'), timestamp = (ctx.message.created_at))
        await ctx.send(embed=embed)
        await ctx.message.guild.create_voice_channel(name=arg, category=ctx.message.channel.category)
    elif type == 'category':
        embed = discord.Embed(colour = (clienthex),title = ('Category'),description = (f'Channel made'), timestamp = (ctx.message.created_at))
        await ctx.send(embed=embed)
        await ctx.message.guild.create_category(name=arg)
