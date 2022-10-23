@client.command(pass_context=True, aliases=['ar'])
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    embed = discord.Embed(colour = (clienthex),title = ('Role added'),description = (f'Role {role.name} was given to {user}'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
