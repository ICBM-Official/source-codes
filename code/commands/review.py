@client.command()
@commands.cooldown(1,21600, commands.BucketType.user)
async def review(ctx):
    DM = client.get_user(ctx.message.author.id)
    revmsg = await DM.send("You will be asked a few questions for the review")
    msg = await DM.send("If you want to cancel at any question type cancel as your answer")
    await asyncio.sleep(2)
    await ctx.send('Review questions sent')

    qu1 = await DM.send("How was your experience:")
    re1 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re1.content =='cancel':
        await revmsg.delete()
        raise ValueError("Cancelled apply")

    qu2 = await DM.send("Would you recommend us to others:")
    re2 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re2.content =='cancel':
        await revmsg.delete()
        raise ValueError("Cancelled apply")

    qu3 = await DM.send("What could be improved on:")
    re3 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re3.content =='cancel':
        await revmsg.delete()
        raise ValueError("Cancelled apply")

    qu4 = await DM.send("How good were the staff:")
    re4 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re4.content =='cancel':
        await revmsg.delete()
        raise ValueError("Cancelled apply")

    qu5 = await DM.send("Other comments:")
    re5 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re5.content =='cancel':
        await revmsg.delete()
        raise ValueError("Cancelled apply")

    qu6 = await DM.send("Rating out of 10:")
    re6 = await client.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re6.content =='cancel':
        await revmsg.delete()
        raise ValueError("Cancelled apply")


    embed = discord.Embed(
        colour = discord.Colour(clienthex),
        title = 'Review',
        description = 'Your review has been sent!',
    )
    msg = await DM.send(embed=embed)
    msg1 = re1.content
    msg2 = re2.content
    msg3 = re3.content
    msg4 = re4.content
    msg5 = re5.content
    msg6 = re6.content
    if len(msg1) > 1024:
        msg1 = 'Message was too long'
    if len(msg2) > 1024:
        msg2 = 'Message was too long'
    if len(msg3) > 1024:
        msg3 = 'Message was too long'
    if len(msg4) > 1024:
        msg4 = 'Message was too long'
    if len(msg5) > 1024:
        msg5 = 'Message was too long'
    if len(msg6) > 1024:
        msg6 = 'Message was too long'
    try:
        rating = int(msg6)
        if rating > 10:
            rating = 10
        def count_multiples(factor, maximum):
            return maximum // factor
        total = (count_multiples(1,rating))

        end = 11 - total
        start = total +1
        bar = ''

        for i in range(1, start):
            bar = bar + '⭐'
        emoji = '<:grey_star:909179980758532116>'

        for i in range(1, end):
            bar = bar + emoji
    except:
        rating = 'None'
        bar = 'No number given'

    await asyncio.sleep(3)
    await revmsg.delete()
    channel = discord.utils.get(ctx.message.guild.channels, name='reviews')
    if channel == None:
        c = await ctx.message.guild.create_text_channel(name=f'reviews', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        channel = discord.utils.get(ctx.message.guild.channels, name='reviews')
    embed = discord.Embed(
        colour = discord.Colour(clienthex),
        timestamp = (ctx.message.created_at),
    )

    embed.set_author(name=ctx.message.author)
    embed.add_field(name='How was your experience in the server:', value=f"{msg1}", inline=False)
    embed.add_field(name='Would you recommend this server to others:', value=f"{msg2}", inline=False)
    embed.add_field(name='What aspects of the server can be improved:', value=f"{msg3}", inline=False)
    embed.add_field(name='How was the experience with the staff:', value=f"{msg4}", inline=False)
    embed.add_field(name='Extra comments:', value=f"{msg5}", inline=False)
    embed.add_field(name=f'Rating: {rating}/10:', value=f"{bar}", inline=False)
    embed.set_footer(text=f"Review" , icon_url=ctx.guild.icon.url)
    await channel.send(ctx.message.author.mention)
    await channel.send(embed=embed)
