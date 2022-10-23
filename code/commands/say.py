@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()
