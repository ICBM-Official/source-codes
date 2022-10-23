@client.command()
async def jumbo(ctx, emoji: Union[discord.Emoji, discord.PartialEmoji]):
    await ctx.message.delete()
    webhook = await ctx.message.channel.create_webhook(name='Jumbo')
    await webhook.send(content=emoji.url, username=ctx.message.author.name, avatar_url=ctx.message.author.avatar.url)
    await webhook.delete()
