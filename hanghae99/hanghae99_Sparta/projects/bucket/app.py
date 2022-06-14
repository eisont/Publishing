from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.msldn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    # 이미 가지고 있는 것을 모두 가지고 와라
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    # 갯수를 새는 len()을 사용해서 현재 저장되어있는 bucket_list를 세서 +1을 합니다.
    count = len(bucket_list) + 1

    doc = {
        # 3가지를 저장해야 합니다. 몇번째인지 알수 있는 번호 num, 버킷 메시지를 나타네는 메시지 text, 진행중인지 진행완료했는지 done
        'num': count,
        'bucket': bucket_receive,
        'done': 0
    }
    db.bucket.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']

    # done 값을 변경해야 합니다. 완료 버튼을 눌렀을 때
    # num_receive는 문자열로 저장되기 때문에 int()를 사용해서 숫자로 변경해야 합니다.
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})

    return jsonify({'msg': '버킷 완료!'})


@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'buckets': bucket_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
