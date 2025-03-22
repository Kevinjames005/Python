import requests
from bs4 import BeautifulSoup

#TODO- Input date.

date = input("Enter the date in YYYY-MM-DD format:")


#TODO - Using web scraping make a list of all songs.
TOP100 = []

# url = f"https://www.billboard.com/charts/hot-100/{date}/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
# }
# response = requests.get(url = url, headers=headers)
# billboard_site = response.text
# soup = BeautifulSoup(billboard_site,"html.parser")
# first_title = soup.find(class_="c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150")
# TOP100.append(first_title.text.strip())
#
# all_title_tags = soup.find_all("h3",class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# for title in all_title_tags:
#     TOP100.append(title.text.strip())
# print(TOP100)

client_id = 'your client id'
client_secret = 'your client secret'

#TODO - Use Spotipy to get user_id, Oauth token and make a playlist of all the songs from above list.
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_uri='http://example.com',
#     scope='user-read-private'
# ))

# user = sp.current_user()
# print("Your Spotify Username / User ID is:", user['id'])

user_id="your user id"

musicURLs = ['https://open.spotify.com/track/6P1t6KqIpTyDRc5ZxsLDn1', 'https://open.spotify.com/track/6mwA6YiKDjAUG8kWvRRUPh', 'https://open.spotify.com/track/5gZEhPrN1VLqTG1nIAXeNK', 'https://open.spotify.com/track/1ckU1EhAO0Nr73QYw24SWJ', 'https://open.spotify.com/track/6nozDLxeL0TE4MS9GqYU1v', 'https://open.spotify.com/track/6DcOZ8pnF5VYveR66L8RCA', 'https://open.spotify.com/track/7mYvtEeBdMqRSyj1Qpv6my', 'https://open.spotify.com/track/1DmCDHic7eiD01WL40tAcB', 'https://open.spotify.com/track/1cjBan0t4eBk2Y5j17hdyf', 'https://open.spotify.com/track/4DJwdQDai9DLYBL9TNrEDo', 'https://open.spotify.com/track/5bGmuxShUba9maPswDnhCs', 'https://open.spotify.com/track/05QUYSOApWLr8oBbpONl7p', 'https://open.spotify.com/track/4GewRLEiI4BDTQsoH8BRVV', 'https://open.spotify.com/track/50MfV7a1pnOEcf2t9kobxW', 'https://open.spotify.com/track/3VEZvzr84WVnoorZ4tlBSw', 'https://open.spotify.com/track/5yaCquc7koPqtgj7v0lwHX', 'https://open.spotify.com/track/0aKWpnMZCR42M9lLhnzJEZ', 'https://open.spotify.com/track/3eYnKe0LhQA1B5HEkQaRTP', 'https://open.spotify.com/track/6WkJ2OK163XXS2oARUC9JM', 'https://open.spotify.com/track/4agp6oHofabdUedr0B1krj', 'https://open.spotify.com/track/3ii5VBrIXJXKEVkjx1IAdP', 'https://open.spotify.com/track/5OQsiBsky2k2kDKy2bX2eT', 'https://open.spotify.com/track/0V4M6Cj5DAWSD9ZyCclTaP', 'https://open.spotify.com/track/4ocbH5ZJqajZIpUrqRUoue', 'https://open.spotify.com/track/0BUoLE4o9eVahDHvTqak67', 'https://open.spotify.com/track/267nfLfaSSDa9ivHncHynh', 'https://open.spotify.com/track/5jbKpvtoxZB14tbnBafMuL', 'https://open.spotify.com/track/6CpyQIHnURl8EDopu20uno', 'https://open.spotify.com/track/4bT2zLVv2T4GiK9q9KtI0v', 'https://open.spotify.com/track/63sLFn6GyiEEYu0EfYg2O9', 'https://open.spotify.com/track/4VSyH8AkIt3kaR5xIPFVVi', 'https://open.spotify.com/track/6x4tKaOzfNJpEJHySoiJcs', 'https://open.spotify.com/track/0LWINYMC4s8QTdDSb1B3Q3', 'https://open.spotify.com/track/6q4aoWgTQ8td2AvqQXuFqm', 'https://open.spotify.com/track/32yottFNSCL9Nho9biIKzY', 'https://open.spotify.com/track/4zGmsDdgSzdfsCNUGjq89Z', 'https://open.spotify.com/track/6sXDEs7z0LLitIPnPBJ4QM', 'https://open.spotify.com/track/6YYd5MLpu45J0uLrMdivF7', 'https://open.spotify.com/track/1yKDl9K9lrbIFSpPBzEQtb', 'https://open.spotify.com/track/2dmeUkbNyWubebnTc7jR58', 'https://open.spotify.com/track/5zmaypMaWb21FUGBxbw8hT', 'https://open.spotify.com/track/4XifD1V0kWoG4WwsXTwS3y', 'https://open.spotify.com/track/1RS3LStQYhju50eBdD9Uul', 'https://open.spotify.com/track/00FROhC5g4iJdax5US8jRr', 'https://open.spotify.com/track/6qc34bnVOyqGDPni8H5W0U', 'https://open.spotify.com/track/5BLzNrrLj2J2TJEv0SyHUh', 'https://open.spotify.com/track/4NTn0Yo8hTGW5tbBANBzfh', 'https://open.spotify.com/track/3rXCZRMiMZp0feGcYXpwYX', 'https://open.spotify.com/track/7pXv5QP8pahWmSw4ccaDKw', 'https://open.spotify.com/track/3jOUUhZ9la9yNijKxdXJwd', 'https://open.spotify.com/track/7kWmT6l911OFlkhhSV6KlM', 'https://open.spotify.com/track/2m1hi0nfMR9vdGC8UcrnwU', 'https://open.spotify.com/track/5E992ekvLksONA86pKVVS0', 'https://open.spotify.com/track/6sIVr2Gk6T5gYzMwrpsUTv', 'https://open.spotify.com/track/7KPcippmg9MvPzb3dzNpQW', 'https://open.spotify.com/track/0YammaEkYSeo9vQYZ1OwS6', 'https://open.spotify.com/track/3KIUKvwteP1HFA5UcvvL11', 'https://open.spotify.com/track/49bDIpHDL6rjqemVbFHry5', 'https://open.spotify.com/track/1zhvxTuSha22nsUT5Nw8gE', 'https://open.spotify.com/track/2GCKWEsbb0Xo1oodTOKVi1', 'https://open.spotify.com/track/0939D7aT18uBDS2MTjWzct', 'https://open.spotify.com/track/3KMsGaN1xdoOaNQELy8vR8', 'https://open.spotify.com/track/2EqmxDTSfBfdLWgeH5Hh4q', 'https://open.spotify.com/track/1i6KuPV0SnkciFR5yJEbty', 'https://open.spotify.com/track/1fadIr5vT3cYEYHNe1fWhv', 'https://open.spotify.com/track/0Eu5f9s4E0xaeHe6fxaNK4', 'https://open.spotify.com/track/6EbHq1fhCZePddEdD5ppui', 'https://open.spotify.com/track/6t8JpJtI0PgVRSuMDGWZlH', 'https://open.spotify.com/track/27vR3JpzHCYUj6f7h7a0GF', 'https://open.spotify.com/track/4eIomBCLTXbjrkrSHnqlgK', 'https://open.spotify.com/track/7yHoWylfxxYpOYkeWT0IqD', 'https://open.spotify.com/track/7w57O4o0xCTn9YpKuaPZDd', 'https://open.spotify.com/track/1D3tgMuJxzaZJMJs8yFVYJ', 'https://open.spotify.com/track/3BsaRV5QIulYz2lV9WWa8T', 'https://open.spotify.com/track/51ZQ1vr10ffzbwIjDCwqm4', 'https://open.spotify.com/track/1DSJNBNhGZCigg9ll5VeZv', 'https://open.spotify.com/track/1uwCYPAgiy5d7lPJvf0gf8', 'https://open.spotify.com/track/5SEBSAio1N77Vbrj1cAEGb', 'https://open.spotify.com/track/6mZI2vbLv1UvlclwDQ4uvc', 'https://open.spotify.com/track/2LgtQEpf5HZ3v3vJ7ccFCd', 'https://open.spotify.com/track/2zS8FkQaSNHAIpqePh95JB', 'https://open.spotify.com/track/6wCbHb0QEEdka3ymfImn4l', 'https://open.spotify.com/track/1wsRitfRRtWyEapl0q22o8', 'https://open.spotify.com/track/5ebtxZRrC1JQvZ1HCAiLYv', 'https://open.spotify.com/track/2g8HN35AnVGIk7B8yMucww', 'https://open.spotify.com/track/3QV7NYkrmV0Q0IHdFJw9hO', 'https://open.spotify.com/track/6sbXGUn9V9ZaLwLdOfpKRE', 'https://open.spotify.com/track/4c6vZqYHFur11FbWATIJ9P', 'https://open.spotify.com/track/3A8pzjcWgAHry1Ix19z7ip', 'https://open.spotify.com/track/5AgCO3dc2kuSicCsw09YCA', 'https://open.spotify.com/track/2ZDxfuXmTIRCdXChbtHpW9', 'https://open.spotify.com/track/0M3ZIWNcizkhYFvn6RuCEz', 'https://open.spotify.com/track/5pinOKTQyPCPpgjIOKVFY3', 'https://open.spotify.com/track/5FVd6KXrgO9B3JPmC8OPst', 'https://open.spotify.com/track/6IPJ7LeWIOhxPW8Sq3nIGc', 'https://open.spotify.com/track/701lky1Ltjfktp6iMSttE0', 'https://open.spotify.com/track/6GhcEJiA224MPuDqyBOzYS', 'https://open.spotify.com/track/72H2JMhXg1f57GH0wyCgy0', 'https://open.spotify.com/track/31KkjOGSf95mMJy4M15T1G', 'https://open.spotify.com/track/5IUceLAshLX0OSTAdSLcPv']
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_uri='http://127.0.0.1:8888/callback',
#     scope='playlist-modify-private playlist-modify-public'
# ))
# for i in TOP100:
#     result = sp.search(q=i, type='track', limit=1)
#     track = result['tracks']['items'][0]
#     musicURLs.append(track['external_urls']['spotify'])
# print(musicURLs)

# TODO - Creating a playlist

# playlist = sp.user_playlist_create(
#     user=user_id,
#     name=f"{date} - Top 100 BillBoard Song",
#     public=False,
#     description="Generated using Spotipy!"
#

#TODO - Adding songs to playlist

playlist_link = "your playlist link"

# sp.playlist_add_items(playlist_id=playlist_link, items=musicURLs)
# print("Successfully Added")




