@client.command()
@commands.has_permissions(manage_messages=True)
async def accept(ctx, member : discord.Member):
    embed = discord.Embed(colour=clienthex, description=f'Congratulations! Your application has been accepted!', timestamp = (ctx.message.created_at))
    embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
    embed.set_thumbnail(url=client.user.avatar.url)
    embed.set_footer(text=ctx.message.guild.name)
    await member.send(embed=embed)
