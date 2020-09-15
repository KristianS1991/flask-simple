from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from appcode.security import authenticate, identity
from appcode.resources.user import UserRegister
from appcode.resources.item import Item, ItemList
from appcode.resources.store import Store, StoreList
from appcode.db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = 'kreeda'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == "__main__":
    app.run(port=5000, debug=True)