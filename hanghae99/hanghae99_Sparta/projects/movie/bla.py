import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    # musics.delete_one(music.select_one('td.info > a.title.ellipsis').text[0:4])
    rank = music.select_one('td.number').text[0:2].strip()  # img 태그의 alt 속성값을 가져오기
    title = music.select_one('td.info > a.title.ellipsis').text[205:257].strip()     # a 태그 사이의 텍스트를 가져오기
    artist = music.select_one('td.info > a.artist.ellipsis').text  # td 태그 사이의 텍스트를 가져오기
    print(rank,title,artist)

# for music in musics:
#     a = music.select_one('td.number')
#     b = music.select_one('td.info > a.title.ellipsis')
#     c = music.select_one('td.info > a.artist.ellipsis')
#     if a is not None:
#         rank = a.text
#         title = b.text
#         artist = c.text
#         print(title,artist)