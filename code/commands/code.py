@client.command(pass_context=True)
async def code(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send("```" + msg.replace("`", "") + "```")
