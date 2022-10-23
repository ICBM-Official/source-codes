@client.command(name='8ball',
            pass_context = True)
async def eight_ball(ctx):
    webhook = await ctx.message.channel.create_webhook(name='selfbot')
    possible_responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
    embed = discord.Embed(colour=0x000001, timestamp=ctx.message.created_at, title='Answer', description=random.choice(possible_responses))
    embed.set_author(name=f"8 Ball", icon_url="https://cdn.discordapp.com/attachments/933743205810327572/959915744831881356/214ogg.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/933743205810327572/959915744831881356/214ogg.jpg")
    embed.set_footer(text=f"{ctx.message.author}")
    await webhook.send(embed=embed, username="8 Ball", avatar_url="https://cdn.discordapp.com/attachments/933743205810327572/959915744831881356/214ogg.jpg")
    await webhook.delete()
