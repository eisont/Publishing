from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.msldn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

movie = db.movies.find_one({'title':'가버나움'})
star = movie['star']

#가버나움과 같은 평점을 가진 영화 제목을 가져와 출력한다.
all_movies = list(db.movies.find({'star': star},{'_id':False}))
# 값이 여러개이기 때문에 for문을 돌리지 않고는 출력이 안되는거 같다.
for m in all_movies:
    print(m['title'])

# 가버나움의 star를 문자열 0으로 바꾸는 코드
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})