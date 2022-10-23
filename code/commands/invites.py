@client.command()
async def invites(ctx, usr : discord.Member):
    if usr == None:
       user = ctx.author
    else:
       user = usr
    total_invites = 0
    for i in await ctx.guild.invites():
        if i.inviter == user:
            total_invites += i.uses
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Invites - {user.name}", icon_url=user.avatar.url)
    embed.set_thumbnail(url=user.avatar.url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    embed.add_field(name="Has invited:", value=total_invites)
    await ctx.send(embed=embed)
    await ctx.message.delete()
