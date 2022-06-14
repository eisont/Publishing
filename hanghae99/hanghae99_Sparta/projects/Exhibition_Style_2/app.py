from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.msldn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index_.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    # 3
    # 클라이언트에서 받은 데이터를 각 변수에 저장합니다.
    image_receive = request.form['image_give']
    exhbn_name_receive = request.form['exhbn_name_give']
    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']

    # 4
    # db에 저장할 객체에 위 변수를 지정합니다.
    doc = {
        'image': image_receive,
        'exhbn_name': exhbn_name_receive,
        'comment': comment_receive,
        'name': name_receive
    }
    # 5
    # 지정한 변수들을 db.homework_2에 저장합니다.
    db.homeworks_2.insert_one(doc)

    # 6
    # 클라이언트에 보낼 msg를 작성합니다.
    return jsonify({'msg': '저장 완료!'})


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
