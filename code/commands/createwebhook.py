@client.command()
@commands.has_permissions(manage_messages=True)
async def createwebhook(ctx, *, arg):
    await ctx.message.delete()
    webhook = await ctx.message.channel.create_webhook(name=arg)
    await webhook.send(content='Webhook made', username=arg)
