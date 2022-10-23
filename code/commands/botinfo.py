@client.command(pass_context=True)
async def botinfo(ctx):
    member = client.user
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}", icon_url=member.avatar.url)
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="User name:", value=member.display_name)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Running on:", value='Inspiration | Powered By Delør', inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()
