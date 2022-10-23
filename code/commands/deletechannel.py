@client.command(pass_context=True , aliases=['deletec'])
@commands.has_permissions(manage_channels=True)
async def deletechannel(ctx, channel_name):
    await ctx.message.delete()
    existing_channel = discord.utils.get(ctx.message.guild.channels, name=channel_name)
    if existing_channel is not None:
        await existing_channel.delete()
        embed = discord.Embed(colour = (clienthex),description = (f'Channel {channel_name} deleted'), timestamp = (ctx.message.created_at))
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour = (clienthex),description = (f'No channel named, "{channel_name}", was found'), timestamp = (ctx.message.created_at))
        await ctx.send(embed=embed)
