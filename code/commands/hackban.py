@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def hackban(ctx, *, member):
    embed = discord.Embed(colour = (clienthex),title = ('Banned'),description = (f'Banned {member}'), timestamp = (ctx.message.created_at))
    embed.set_author(name=f"{member}", icon_url=member.avatar.url)
    embed.set_thumbnail(url=member.avatar.url)
    try:
        await ctx.guild.ban(discord.Object(id=member))
        await ctx.send(embed=embed)
        await ctx.message.delete()
    except:
        embed = discord.Embed(colour = (clienthex),description = (f"Couldn't find member"), timestamp = (ctx.message.created_at))
        await ctx.send(embed=embed)
        await ctx.message.delete()
