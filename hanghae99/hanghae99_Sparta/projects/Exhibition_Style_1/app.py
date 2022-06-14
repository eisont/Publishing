from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.msldn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# data = requests.get('http://ticket.interpark.com/TPGoodsList.asp?Ca=Eve&SubCa=Eve_O', headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')
#
# musics = soup.select('table > tr > td > .sR_w755 > .Rk_gen2 > .con > .stit > table > tbody > tr')

# for exhi in musics:
#     place = exhi.select_one('td.Rkdate > a').text
#     a_tag = exhi.select_one('td.RKtxt')
#
# if a_tag is not None:
#     title = exhi.select_one('span.fw_bold > a')
#     image = exhi.select_one('img')


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    # 3
    # 클라이언트에서 받은 데이터를 각 변수에 저장합니다.
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    image_receive = request.form['image_give']
    exhbn_name_receive = request.form['exhbn_name_give']

    # 4# db에 저장할 객체에 위 변수를 지정합니다.
    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'image': image_receive,
        'exhbn_name': exhbn_name_receive
    }
    #5
    # 지정한 변수들을 db.homework_2에 저장합니다.
    db.homeworks_2.insert_one(doc)

    # 6
    # 클라이언트에 보낼 msg를 작성합니다.
    return jsonify({'msg': '기록 완료!'})


@app.route("/homework", methods=["GET"])
def homework_get():
    # 1
    # 서버를 먼저 제작합니다.#order_list라는 변수에 db에 있는 모든 정보를 가지고 옵니다.
    order_list = list(db.homeworks_2.find({}, {'_id': False}))
    # 2
    # order_list에 저장한 정보를 orders에 담아 클라이언트에 보냅니다.
    return jsonify({'orders': order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
