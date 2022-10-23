@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit=50, member: discord.Member=None):
    await ctx.message.delete()
    msg = []
    try:
        limit = int(limit)
    except:
        embed = discord.Embed(colour = (clienthex),description = ("Please pass in an integer as limit"), timestamp = (ctx.message.created_at))
        return await ctx.send(embed=embed)
    if not member:
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(colour = (clienthex),description = (f"Purged {limit} messages"), timestamp = (ctx.message.created_at))
        return await ctx.send(embed=embed, delete_after=3)
    async for m in ctx.channel.history():
        if len(msg) == limit:
            break
        if m.author == member:
            msg.append(m)
    await ctx.channel.delete_messages(msg)
    embed = discord.Embed(colour = (clienthex),description = (f"Purged {limit} messages of {member.mention}"), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed, delete_after=3)
