@client.command()
@commands.has_permissions(manage_emojis=True)
async def addemoji(ctx, *, name):
    qul = await ctx.send("Upload your emoji")
    rel = await client.wait_for('message' ,check=(lambda message: message.author == ctx.message.author))
    for file in os.listdir("./"):
        if file.endswith(".jpg"):
            os.remove(file)
    for attachment in rel.attachments:
        await attachment.save(fp='emoji.jpg')
    with open('emoji.jpg', 'rb') as image:
        img_byte = image.read()
        await ctx.message.guild.create_custom_emoji(name = (name), image = img_byte)
    for file in os.listdir("./"):
        if file.endswith(".jpg"):
            os.remove(file)
    await ctx.message.delete()
    await qul.delete()
    await rel.delete()
    embed = discord.Embed(colour = (clienthex),title = ('Emoji'),description = (f'Emoji uploaded'), timestamp = (ctx.message.created_at))
    embed.set_thumbnail(url='emoji.jpg')
    await ctx.send(embed=embed)
    for file in os.listdir("./"):
        if file.endswith(".jpg"):
            os.remove(file)
