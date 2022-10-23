@client.command()
@commands.has_permissions(manage_channels=True)
async def replace(ctx, type : str, *, arg):
    await ctx.message.delete()
    if arg == None:
        embed = discord.Embed(colour = (clienthex),title = ('Channel'),description = (f'Channel not found'), timestamp = (ctx.message.created_at))
        await ctx.send(embed=embed)
    elif type == 'text':
        channel = discord.utils.get(ctx.guild.channels, name=arg)
        if channel == None:
            embed = discord.Embed(colour = (clienthex),title = ('Channel'),description = (f'Channel not found'), timestamp = (ctx.message.created_at))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour = (clienthex),title = ('Text'),description = (f'Channel replaced'), timestamp = (ctx.message.created_at))
            await ctx.send(embed=embed)
            await ctx.message.guild.create_text_channel(name=channel.name, category=channel.category, topic=channel.topic)
            await channel.delete()
    elif type == 'voice':
        channel = discord.utils.get(ctx.guild.channels, name=arg)
        if channel == None:
            embed = discord.Embed(colour = (clienthex),title = ('Channel'),description = (f'Channel not found'), timestamp = (ctx.message.created_at))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour = (clienthex),title = ('Voice'),description = (f'Channel replaced'), timestamp = (ctx.message.created_at))
            await ctx.send(embed=embed)
            await ctx.message.guild.create_voice_channel(name=channel.name, category=channel.category)
            await channel.delete()
    elif type == 'category':
        channel = discord.utils.get(ctx.guild.categories, name=arg)
        if channel == None:
            embed = discord.Embed(colour = (clienthex),title = ('Channel'),description = (f'Channel not found'), timestamp = (ctx.message.created_at))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour = (clienthex),title = ('Category'),description = (f'Channel replaced'), timestamp = (ctx.message.created_at))
            await ctx.send(embed=embed)
            await ctx.message.guild.create_category(name=channel.name)
            await channel.delete()
