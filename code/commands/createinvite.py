@client.command(aliases=['cinv', 'makeinvite'])
@commands.has_permissions(create_instant_invite=True)
async def createinvite(ctx, channel: discord.TextChannel):
    invite = await channel.create_invite(unique=True, reason=f"{ctx.author} user createinvite")
    embed = discord.Embed(title="Instant Invite Created",description=f"{ctx.author.mention}, here is your newly created instant invite:\n"f"{invite.url}",colour=discord.Colour(clienthex), timestamp = (ctx.message.created_at))
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()
