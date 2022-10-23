@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member, *, reason=None):
    guild = ctx.guild
    if discord.utils.get(guild.roles, name="Muted"):
        pass
    else:
        await guild.create_role(name="Muted", colour=discord.Colour(0x939995))
        print('role made mute')

    role = discord.utils.get(ctx.message.author.guild.roles, name='Muted')
    await member.add_roles(role)
    embed = discord.Embed(colour = (clienthex),title = ('Muted'),description = (f'Muted {member}'), timestamp = (ctx.message.created_at))
    embed.set_author(name=f"{member}", icon_url=member.avatar.url)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name='Reason', value=(f"""{reason}"""), inline=False)
    await ctx.send(embed=embed)
    embed = discord.Embed(colour = (clienthex),title = ('Muted'),description = (f'You have been muted! {member}'), timestamp = (ctx.message.created_at))
    embed.set_author(name=f"{member}", icon_url=member.avatar.url)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name='Reason', value=(f"""{reason}"""), inline=False)
    await member.send(embed=embed)
    await ctx.message.delete()
