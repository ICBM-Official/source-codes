@client.command(pass_context=True, aliases=['ld'])
@commands.has_permissions(manage_messages=True)
async def lock(ctx, role : discord.Role = None):
    role = ctx.guild.default_role if not role else role
    await ctx.channel.set_permissions(role, send_messages=False)
    embed = discord.Embed(colour = (clienthex),title = ('Locked'),description = (f'This channel has been locked!'), timestamp = (ctx.message.created_at))
    lm = await ctx.send(embed=embed)
    await ctx.message.delete()
