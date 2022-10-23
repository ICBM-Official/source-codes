@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def quote(ctx, *, arg):
    qim2 = await ctx.send("What do you want to say:")
    con = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour(clienthex),
        timestamp = (ctx.message.created_at),


        )
    embed.set_author(name=ctx.message.author, icon_url=client.user.avatar.url)
    embed.set_thumbnail(url=client.user.avatar.url)
    embed.add_field(name=arg, value=(con.content), inline=False)
    msg = await channel.send(embed=embed)
    await ctx.message.delete()
    await con.delete()
    await qim2.delete()
