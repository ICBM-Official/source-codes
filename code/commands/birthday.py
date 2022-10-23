@client.command()
async def birthday(ctx, member : discord.Member):
    api_key=""
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key, "birthday", limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
    embed = discord.Embed(
            colour = discord.Colour(clienthex),
            timestamp = (ctx.message.created_at),
            description = (f"Make sure to wish {member.name} a happy birthday"),
            )
    embed.set_author(name=f"🎉 It's {member.name}'s bithday today!", icon_url=member.avatar.url)
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(text=ctx.message.guild.name)
    embed.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🎉')
    await ctx.message.delete()
