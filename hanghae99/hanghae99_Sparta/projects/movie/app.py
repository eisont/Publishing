from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
# bs4 와 BeautifulSoup 사용하기 위한 코드

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.msldn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
# db와 연결하기 위한 코드

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    # 위 변수를 가지고 크롤링을 해야합니다.
    # meta_prac에 크롤링한게 있습니다. 그것을 복붙합시다.

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    # 받아온 url을 사용하기 위해 위에 복붙합니다.

    soup = BeautifulSoup(data.text, 'html.parser')

    # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']
    # 이제 db에 저장해야합니다.
    # 그러기 위해서는 dbprac(파일 이름)을 가지고 와서 사용해야 합니다.

    # db 저장 코드
    doc = {
        'title': title,
        'image': image,
        'desc': desc,
        'star': star_receive,
        'comment': comment_receive
    }
    db.movies.insert_one(doc)

    return jsonify({'msg':'저장 완료'})
    #서버 완료

@app.route("/movie", methods=["GET"])
def movie_get():
    # 서버를 만들어 봅시다.
    # 전체 데이터를 받아오겠습니다.
    movie_list = list(db.movies.find({},{'_id':False}))

    return jsonify({'movies':movie_list})
    # movie_list를 movies로 보내겠습니다.
    # 서버 끝

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)