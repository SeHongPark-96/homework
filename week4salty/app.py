from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 여길 채워나가세요!
    #1. 클라이언트로부터 데이터 받기
    name_get = request.form['name_give']
    count_get = request.form['count_give']
    address_get = request.form['address_give']
    phone_get = request.form['phone_give']

    #2. mongoDB에 데이터 넣기
    order = {
        'name' : name_get,
    'count' : count_get,
    'address' : address_get,
    'phone' : phone_get
    }
    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg' : '주문이 완료되었습니다'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 여길 채워나가세요!
    # mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기
    orders = list(db.orders.find({},{'_id' : False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)