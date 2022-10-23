@client.command(pass_context=True, aliases=['rn'])
@commands.has_permissions(manage_roles=True)
async def rolename(ctx, role: discord.Role, *, arg):
    await role.edit(name=arg)
    embed = discord.Embed(colour = (clienthex), title = ('Role edit'), description = (f'Role {role} name changed to {arg}'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
