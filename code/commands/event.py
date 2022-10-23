@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def event(ctx, channel : discord.TextChannel, *, arg):
    qim2 = await ctx.send("Ping? [y/n]")
    con = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if con.content == 'y' or con.content == 'Y':
        embed = discord.Embed(
            colour = discord.Colour(clienthex),
            timestamp = (ctx.message.created_at),
        )
        embed.set_author(name=ctx.message.author, icon_url=client.user.avatar.url)
        embed.set_thumbnail(url=client.user.avatar.url)
        embed.add_field(name='Event', value=(arg), inline=False)
        msg = await channel.send('@everyone')
        msg = await channel.send(embed=embed)
        await ctx.message.delete()
        await qim2.delete()
        await con.delete()
    else:
        embed = discord.Embed(
            colour = discord.Colour(clienthex),
            timestamp = (ctx.message.created_at),
        )
        embed.set_author(name=ctx.message.author, icon_url=client.user.avatar.url)
        embed.set_thumbnail(url=client.user.avatar.url)
        embed.add_field(name='Event', value=(arg), inline=False)
        msg = await channel.send(embed=embed)
        await ctx.message.delete()
        await qim2.delete()
        await con.delete()
