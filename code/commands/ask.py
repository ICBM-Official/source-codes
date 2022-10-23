@client.command(pass_context = True)
async def ask(ctx):
    possible_responses = [
        'Yes ',
        'No ',
    ]
    embed = discord.Embed(colour=clienthex, timestamp=ctx.message.created_at, title='Answer', description=random.choice(possible_responses))
    embed.set_author(name=f"?", icon_url=ctx.message.author.avatar.url)
    embed.set_thumbnail(url=ctx.message.author.avatar.url)
    embed.set_footer(text=f"{ctx.message.author}")
    await ctx.send(embed=embed)
