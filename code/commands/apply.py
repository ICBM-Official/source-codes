@client.command()
@commands.cooldown(1,21600, commands.BucketType.user)
async def apply(ctx):
    DM = client.get_user(ctx.message.author.id)
    appmsg = await DM.send("You will be asked a few questions in order to apply")
    msg = await DM.send("If you want to cancel at any question type cancel as your answer")
    await asyncio.sleep(2)
    await ctx.send('Apply questions sent')

    qu1 = await DM.send("What are you applying for:")
    re1 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re1.content =='cancel':
        await appmsg.delete()
        raise ValueError("Cancelled apply")

    qu2 = await DM.send("Discord username and tag:")
    re2 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re2.content =='cancel':
        await appmsg.delete()
        raise ValueError("Cancelled apply")

    qu3 = await DM.send("State your age:")
    re3 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re3.content =='cancel':
        await appmsg.delete()
        raise ValueError("Cancelled apply")

    qu4 = await DM.send("Please state your experience. **Be as descriptive as you can**:")
    re4 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re4.content =='cancel':
        await appmsg.delete()
        raise ValueError("Cancelled apply")

    qu5 = await DM.send("Why do you think you are an ideal candidate for the job you're applying for? **Be as descriptive as you can**:")
    re5 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re5.content =='cancel':
        await appmsg.delete()
        raise ValueError("Cancelled apply")

    qu6 = await DM.send("Is there anything else you wish to add:")
    re6 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re6.content =='cancel':
        await appmsg.delete()
        raise ValueError("Cancelled apply")

    embed = discord.Embed(
        colour = discord.Colour(clienthex),
        title = 'Application',
        description = 'Your application has been sent!',
    )
    msg = await DM.send(embed=embed)

    msg1 = re1.content
    msg2 = re2.content
    msg3 = re3.content
    msg4 = re4.content
    msg5 = re5.content
    msg6 = re6.content
    if len(msg1) > 3000:
        msg1 = 'Message was too long'
    if len(msg2) > 3000:
        msg2 = 'Message was too long'
    if len(msg3) > 3000:
        msg3 = 'Message was too long'
    if len(msg4) > 3000:
        msg4 = 'Message was too long'
    if len(msg5) > 3000:
        msg5 = 'Message was too long'
    if len(msg6) > 3000:
        msg6 = 'Message was too long'
    await asyncio.sleep(3)
    await appmsg.delete()
    channel = discord.utils.get(ctx.message.guild.channels, name='applications')
    if channel == None:
        c = await ctx.message.guild.create_text_channel(name=f'applications', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        channel = discord.utils.get(ctx.message.guild.channels, name='applications')
    embed1 = discord.Embed(
        colour = discord.Colour(clienthex),
        title = ('Applying for:'),
        description = (f"{msg1}"),
    )
    embed1.set_author(name=ctx.message.author)
    embed2 = discord.Embed(
        colour = discord.Colour(clienthex),
        title = ('Tag:'),
        description = (f"{msg2}"),
    )
    embed2.set_author(name=ctx.message.author)
    embed3 = discord.Embed(
        colour = discord.Colour(clienthex),
        title = ('Age:'),
        description = (f"{msg3}"),
    )
    embed3.set_author(name=ctx.message.author)
    embed4 = discord.Embed(
        colour = discord.Colour(clienthex),
        title = ('Previous experiences:'),
        description = (f"{msg4}"),
    )
    embed4.set_author(name=ctx.message.author)
    embed5 = discord.Embed(
        colour = discord.Colour(clienthex),
        title = ('Ideal candidate:'),
        description = (f"{msg5}"),
    )
    embed5.set_author(name=ctx.message.author)
    embed6 = discord.Embed(
        colour = discord.Colour(clienthex),
        title = ('Extra:'),
        description = (f"{msg6}"),
    )
    embed6.set_author(name=ctx.message.author)
    await channel.send(ctx.message.author.mention)
    await asyncio.sleep(1)
    await channel.send(embed=embed1)
    await asyncio.sleep(1)
    await channel.send(embed=embed2)
    await asyncio.sleep(1)
    await channel.send(embed=embed3)
    await asyncio.sleep(1)
    await channel.send(embed=embed4)
    await asyncio.sleep(1)
    await channel.send(embed=embed5)
    await asyncio.sleep(1)
    await channel.send(embed=embed6)
