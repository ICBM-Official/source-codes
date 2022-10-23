@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def nickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(colour = (clienthex),description = (f'Nickname was changed for {member.mention}'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
