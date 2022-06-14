client = MongoClient('mongodb+srv://test:sparta@cluster0.msldn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for mmm in movies:
    a = mmm.select_one('td:nth-child(1) > img')
    b = mmm.select_one('td.title > div > a')
    c = mmm.select_one('td.point')
    if a is not None:
        doc = {
            'title':b.text,
            'rank':a['alt'],
            'star':c.text
        }
        db.movies.insert_one(doc)
        # print(a['alt'],b.text,c.text)