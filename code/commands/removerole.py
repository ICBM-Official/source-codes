@client.command(pass_context=True, aliases=['rr'])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    embed = discord.Embed(colour = (clienthex),title = ('Role removed'),description = (f'Role {role.name} was removed from {user}'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
