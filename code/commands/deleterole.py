@client.command(pass_context=True, aliases=['dr'])
@commands.has_permissions(manage_roles=True)
async def deleterole(ctx, role_name):
    role = discord.utils.get(ctx.message.guild.roles, name=role_name)
    await role.delete()
    embed = discord.Embed(colour = (clienthex), title = ('Role deleted'), description = (f'Role {role} was deleted'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
