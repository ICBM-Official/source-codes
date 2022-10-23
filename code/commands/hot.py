@client.command(aliases=["howhot", "hot"])
async def hotcalc(ctx, *, user: discord.Member = None):
    user = user or ctx.author

    r = random.randint(1, 100)
    hot = r / 1.17

    if hot > 75:
        emoji = "💞"
    elif hot > 50:
        emoji = "💖"
    elif hot > 25:
        emoji = "❤"
    else:
        emoji = "💔"

    q='hot'

    api_key=""
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=f"**{user.name}** is **{hot:.2f}%** hot {emoji}")
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)

    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
