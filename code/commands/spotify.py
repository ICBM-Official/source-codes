sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='', client_secret=''))

@client.command()
async def spotify(ctx, *, search):

    searchResults = sp.search(q=search, type="track", limit=1, market="US")
    items = searchResults['tracks']['items']
    name = 'none'
    if len(items) > 0:
        song = items[0]
        id = song['id']
        meta = sp.track(id)
        features = sp.audio_features(id)

        name = meta['name']
        album = meta['album']['name']
        artist = meta['album']['artists'][0]['name']
        release_date = meta['album']['release_date']
        length = meta['duration_ms']
        popularity = meta['popularity']
        explicit = meta['explicit']
        image = meta['album']['images'][0]['url']

        acousticness = features[0]['acousticness']
        danceability = features[0]['danceability']
        energy = features[0]['energy']
        instrumentalness = features[0]['instrumentalness']
        liveness = features[0]['liveness']
        loudness = features[0]['loudness']
        speechiness = features[0]['speechiness']
        tempo = features[0]['tempo']
        valence = features[0]['valence']
        time_signature = features[0]['time_signature']
        url = f"https://open.spotify.com/track/{id}"

        millis = int(length)
        seconds=(millis/1000)%60
        seconds = int(seconds)
        minutes=(millis/(1000*60))%60
        minutes = int(minutes)
        hours=(millis/(1000*60*60))%24
        length =  ("%d:%02d:%02d" % (hours, minutes, seconds))

    embed = discord.Embed(colour=0x1DB954, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Spotify Search", icon_url="https://cdn.discordapp.com/attachments/730456139111858336/909859703473995846/spotify-icon-marilyn-scott-0.png")
    embed.set_thumbnail(url=image)
    embed.set_image(url=image)
    embed.set_footer(text=f"React with 🔊 to view audio features")
    embed.add_field(name="Track", value=f"**__[{name}]({url})__**", inline=False)
    embed.add_field(name="Album", value=album, inline=True)
    embed.add_field(name="Artist", value=artist, inline=True)
    message = await ctx.send(embed=embed)

    await message.add_reaction("🎵")
    await message.add_reaction("🔊")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["🔊", "🎵"]

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji) == "🎵":
                embed = discord.Embed(colour=0x1DB954, timestamp=ctx.message.created_at)
                embed.set_author(name=f"Spotify Search", icon_url="https://cdn.discordapp.com/attachments/730456139111858336/909859703473995846/spotify-icon-marilyn-scott-0.png")
                embed.set_thumbnail(url=image)
                embed.set_image(url=image)
                embed.set_footer(text=f"React with 🔊 to view audio features")
                embed.add_field(name="Track", value=f"**__[{name}]({url})__**", inline=False)
                embed.add_field(name="Album", value=album, inline=True)
                embed.add_field(name="Artist", value=artist, inline=True)
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "🔊":
                embed = discord.Embed(colour=0x1DB954, timestamp=ctx.message.created_at, description=f'Audio features for **__[{name}]({url})__**')
                embed.set_author(name=f"Spotify Search", icon_url="https://cdn.discordapp.com/attachments/730456139111858336/909859703473995846/spotify-icon-marilyn-scott-0.png")
                embed.set_thumbnail(url=image)
                embed.set_footer(text=f"React with 🎵to view song details")
                embed.add_field(name="Release date", value=release_date, inline=True)
                embed.add_field(name="Length", value=length, inline=True)
                embed.add_field(name="Popularity", value=popularity, inline=True)
                embed.add_field(name="Acousticness", value=acousticness, inline=False)
                embed.add_field(name="Danceability", value=danceability, inline=False)
                embed.add_field(name="Energy", value=energy, inline=False)
                embed.add_field(name="Instrumentalness", value=instrumentalness, inline=False)
                embed.add_field(name="Liveness", value=liveness, inline=False)
                embed.add_field(name="Loudness", value=loudness, inline=False)
                embed.add_field(name="Speechiness", value=speechiness, inline=False)
                embed.add_field(name="Tempo", value=tempo, inline=False)
                embed.add_field(name="Valence", value=valence, inline=False)
                embed.add_field(name="Explicit", value=explicit, inline=False)
                embed.add_field(name="Time_signature", value=time_signature, inline=False)
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)
            elif cur_page == pages:
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.remove_reaction('🔊', client.user)
            await message.remove_reaction('🎵', client.user)
