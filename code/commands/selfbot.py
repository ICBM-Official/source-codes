@client.command()
@commands.has_permissions(manage_messages=True)
async def selfbot(ctx, *, arg):
    await ctx.message.delete()
    webhook = await ctx.message.channel.create_webhook(name='selfbot')
    await webhook.send(content=arg, username=ctx.message.author.name, avatar_url=ctx.message.author.avatar.url)
    await webhook.delete()
