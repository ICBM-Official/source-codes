@client.group(pass_context=True, invoke_without_command=True)
async def ascii(ctx, *, msg):
    if ctx.invoked_subcommand is None:
        if msg:
            msg = str(figlet_format(msg.strip()))
            if len(msg) > 2000:
                await ctx.send('Message too long, RIP.')
            else:
                await ctx.send('```\n{}\n```'.format(msg))
        else:
            await ctx.send(
                           'Please input text to convert to ascii art. Ex: ``>ascii stuff``')
