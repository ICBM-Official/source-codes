@client.command()
async def gif(ctx, search=None):
    if search == None:
        q='hello'
    else:
        q=seach

    api_key=""
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=f'Woof!')
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
