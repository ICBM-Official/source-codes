@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name='Muted')
    await member.remove_roles(role)
    embed = discord.Embed(colour = (clienthex),title = ('Muted'),description = (f'You have been unmuted! {member}'), timestamp = (ctx.message.created_at))
    embed.set_author(name=f"{member}", icon_url=member.avatar.url)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name='Reason', value=(f"""{reason}"""), inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()
