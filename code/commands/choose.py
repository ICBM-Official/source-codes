@client.command(pass_context = True)
async def choose(ctx, *choices: str):
    emb = (discord.Embed(color=clienthex, description = random.choice(choices)))
    emb.set_thumbnail(url=ctx.message.author.avatar.url)
    emb.set_footer(text=f"{ctx.message.author}")
    emb.set_author(name=f"Chooser", icon_url=ctx.message.author.avatar.url)
    await ctx.send(embed=emb)
