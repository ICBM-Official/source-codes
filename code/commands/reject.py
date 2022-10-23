@client.command()
@commands.has_permissions(manage_messages=True)
async def reject(ctx, member : discord.Member):
    embed = discord.Embed(colour=clienthex, description=f'Thank you for your application. Unfortunately we have declined your application as we are not currently looking for any support.', timestamp = (ctx.message.created_at))
    embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
    embed.set_thumbnail(url=client.user.avatar.url)
    embed.set_footer(text=ctx.message.guild.name)
    await member.send(embed=embed)
