@client.command()
@commands.has_permissions(manage_messages=True)
async def echo(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)
