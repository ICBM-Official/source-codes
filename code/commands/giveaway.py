@client.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, *, arg):
    qim2 = await ctx.send("End Date:")
    con = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    qim3 = await ctx.send("Ping? [y/n]")
    con2 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if con2.content == 'y' or con2.content == 'Y':
        embed = discord.Embed(
                colour = discord.Colour(clienthex),
                timestamp = (ctx.message.created_at),
                )
        embed.set_author(name="Giveaway!", icon_url=client.user.avatar.url)
        embed.set_thumbnail(url=client.user.avatar.url)
        embed.add_field(name="End Date:", value=con.content ,inline=False)
        embed.add_field(name="Prize:", value=arg ,inline=False)
        embed.add_field(name="React To The Giveaway To Join", value="-------------------------------------" ,inline=False)
        embed.set_footer(text=ctx.message.guild.name)
        msg = await ctx.send('@everyone')
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🎉')
        await ctx.message.delete()
        await qim2.delete()
        await con.delete()
        await qim3.delete()
        await con2.delete()
    else:
        embed = discord.Embed(
                colour = discord.Colour(clienthex),
                timestamp = (ctx.message.created_at),
                )
        embed.set_author(name="Giveaway!", icon_url=client.user.avatar.url)
        embed.set_thumbnail(url=client.user.avatar.url)
        embed.add_field(name="End Date:", value=con.content ,inline=False)
        embed.add_field(name="Prize:", value=arg ,inline=False)
        embed.add_field(name="React To The Giveaway To Join", value="-------------------------------------" ,inline=False)
        embed.set_footer(text=ctx.message.guild.name)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🎉')
        await ctx.message.delete()
        await qim2.delete()
        await con.delete()
        await qim3.delete()
        await con2.delete()
