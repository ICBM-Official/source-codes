@client.command(pass_context = True)
async def flip(ctx):
    flip = ['Heads','Tails']
    emb = (discord.Embed(color=clienthex, description = random.choice(flip)))
    emb.set_thumbnail(url=ctx.message.author.avatar.url)
    emb.set_footer(text=f"{ctx.message.author}")
    emb.set_author(name=f"Heads or Tails", icon_url=ctx.message.author.avatar.url)
    await ctx.send(embed=emb)
