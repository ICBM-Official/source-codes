@client.command()
async def streaming(ctx, user: discord.Member = None):
    for activity in user.activities:
        if isinstance(activity, discord.Streaming):
            url = activity.url
            embed = discord.Embed(
                title = f"{user.name}'s Twitch",
                description = f'{user} is streaming on twitch: {url}',
                colour = 0x6441a5,
            )
            embed.set_author(name='Twitch', icon_url='https://cdn.discordapp.com/attachments/730456139111858336/919221566015946823/CStinzn-_400x400.jpg')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/730456139111858336/919221566015946823/CStinzn-_400x400.jpg')
            await ctx.send(embed=embed)
            await ctx.message.delete()
