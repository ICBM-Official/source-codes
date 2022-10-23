@client.command(name="poll")
@commands.has_permissions(manage_messages=True)
async def poll(ctx, *, title):
    embed = discord.Embed(
        title="A new poll has been created!",
        description=f"{title}",
        color= discord.Colour(clienthex),
        timestamp = (ctx.message.created_at),
    )
    embed.set_footer(
        text=f"Poll created by: {ctx.message.author} • React to vote!"
    )
    embed_message = await ctx.send(embed=embed)
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")
    await embed_message.add_reaction("🤷")
