@client.command(pass_context=True)
async def l2g(ctx, *, msg: str, aliases=['lmgtfy']):
    lmgtfy = 'http://lmgtfy.com/?q='
    await ctx.send(lmgtfy + urllib.parse.quote_plus(msg.lower().strip()))
