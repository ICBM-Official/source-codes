@client.command(pass_context=True, aliases=['cr'])
@commands.has_permissions(manage_roles=True)
async def createrole(ctx, *, arg):
    guild = ctx.guild
    author = ctx.message.author
    await guild.create_role(name=arg)
    embed = discord.Embed(colour = (clienthex),title = ('Role created'),description = (f'Role {arg} was created'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
