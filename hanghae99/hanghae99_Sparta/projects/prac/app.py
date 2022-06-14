from flask import Flask, render_template, request, jsonify
# Flask, render_template, request, jsonify(=프레임워크)를 사용하기 위해서는 이쪽에 작성해야 합니다.
app = Flask(__name__)
# flask 프레임워크는 서버를 구동시켜주는 편한 코드 모음입니다.

@app.route('/')
def home():
   return render_template('index.html')
# 내가 만든 index.html 파일을 / 서버와 연결해서 화면에 출력해줍니다.

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   # title_give라는 뭔가를 받아와서
   # title_receive 변수에 저장합니다.
   print(title_receive)
   # title_receive를 찍어줍니다.
   return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})
   #이것을 /test 창구에 받아 사용합니다.


@app.route('/test', methods=['POST'])
# 우리가 /test라는 창구를 만들었고 이 창구에서 post 방식으로 받는 것은 이쪽으로 오세요.
def test_post():
   title_receive = request.form['title_give']
   # title_give라는 뭔가를 받아와서
   # title_receive 변수에 저장합니다.
   print(title_receive)
   return jsonify({'result': 'success', 'msg': '요청을 잘 받았어요!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)