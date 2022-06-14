# flask를 사용하기 위한 코드
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# db를 사용하기 위해 밑에 3줄은 복붙하겠습니다.
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.msldn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def web_mars_post():
    # 3
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    # 위 변수를 db에 저장해야 합니다.

    # 4
    doc = {
        'name': name_receive,
        # name에 name_receive 변수를 띄우겠습니다.
        'address': address_receive,
        # address에 address_receive 변수를 띄우겠습니다.
        'size': size_receive
        # size에 size_receive 변수를 띄우겠습니다.
    }
    # 5
    db.mars.insert_one(doc)
    # db의 mars창구에 doc 변수를 저장합니다.

    # 6
    return jsonify({'msg': '주문완료!'})
    # 버튼이 눌리면 msg가 띄워집니다.(=alert)


@app.route("/mars", methods=["GET"])
def web_mars_get():
    # 1
    # 서버를 먼저 만듭니다.
    # db에서 모든 주문을 받아와야 합니다.
    order_list = list(db.mars.find({}, {'_id': False}))
    # find{} 이 안에는 조건이 들어갑니다. 조건이 없기 때문에 빈공간으로 사용합니다.
    # order_list는 우리가 화성땅 공동구매 사이트에 작성한 데이터를 저장한 변수입니다.

    # 2
    return jsonify({'orders': order_list})
    # order_list로 모든 정보를 받아와서 'orders' 에 보내줍니다.


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
