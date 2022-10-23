@client.command()
async def translate(ctx, country, *,arg):
    translator = Translator()
    translation = translator.translate(arg, dest=country)
    translation_message = (f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    embed = discord.Embed(title='Translator', description=translation_message, colour=clienthex, timestamp=ctx.message.created_at)
    embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar.url)
    await ctx.send(embed=embed)
