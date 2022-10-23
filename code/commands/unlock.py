@client.command(pass_context=True, aliases=['ul'])
@commands.has_permissions(manage_messages=True)
async def unlock(ctx, role : discord.Role = None):
    role = ctx.guild.default_role if not role else role
    await ctx.channel.set_permissions(role, send_messages=True)
    embed = discord.Embed(colour = (clienthex),title = ('Unlocked'),description = (f'This channel has now been unlocked'), timestamp = (ctx.message.created_at))
    lm = await ctx.send(embed=embed)
    await ctx.message.delete()
