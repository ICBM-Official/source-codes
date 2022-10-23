@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def massban(ctx, users: Greedy[User], *, arg=None):
    for user in users:
        await user.ban(reason=arg)
    await ctx.message.delete()
    embed = discord.Embed(colour = (clienthex),title = ('Massban'),description = (f'Banned all users sent'), timestamp = (ctx.message.created_at))
    embed.add_field(name='Users', value=(f"""{users}"""), inline=False)
    embed.add_field(name='Reason', value=(f"""{arg}"""), inline=False)
    await ctx.send(embed=embed)
