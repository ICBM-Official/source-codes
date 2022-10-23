@client.command()
@commands.has_permissions(manage_roles=True)
async def rolecount(ctx, *, arg):
    guild = client.get_guild(int(ctx.message.guild.id))
    role = discord.utils.get(guild.roles, name=arg)
    user_count = len(role.members)
    embed = discord.Embed(colour = (clienthex), title = ('Role count'), description = (f'There are {user_count} members with the role {role}'), timestamp = (ctx.message.created_at))
    await ctx.send(embed=embed)
    await ctx.message.delete()
