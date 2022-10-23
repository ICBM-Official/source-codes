@client.command()
async def codeblock(ctx, * , message : discord.Message):
    await ctx.send(f'```{message.content}```')
