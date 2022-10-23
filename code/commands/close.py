@client.command(pass_context=True , aliases=['ct', 'closet'])
@commands.has_permissions(manage_messages=True)
async def close(ctx, channel : discord.TextChannel = None):
    channel = ctx.message.channel if not channel else channel
    tauth = ctx.message.author
    if ('ticket-logs') in channel.name:
        pass
    elif ('ticket') in channel.name:
        ticket = client.get_channel(channel.id)
        guild = client.get_guild(tauth.guild.id)
        logs = discord.utils.get(guild.channels, name='ticket-logs')
        embed = discord.Embed(
            colour = discord.Colour(clienthex),
            title = (f'{ctx.message.channel.name} was closed by {ctx.message.author}'),
        )
        await logs.send(embed=embed)
        await ticket.delete()
    elif ('report') in channel.name:
        ticket = client.get_channel(channel.id)
        guild = client.get_guild(tauth.guild.id)
        logs = discord.utils.get(guild.channels, name='ticket-logs')
        embed = discord.Embed(
            colour = discord.Colour(clienthex),
            title = (f'{ctx.message.channel.name} was closed by {ctx.message.author}'),
        )
        await logs.send(embed=embed)
        await ticket.delete()
    else:
        pass
