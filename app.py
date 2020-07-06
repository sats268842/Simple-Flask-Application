from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from datetime import timedelta
import sys
import logging

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']= False
app.secret_key = "santhosh"
api =Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
jwt = JWT(app, authenticate, identity)



api.add_resource(Item, '/item/<string:name>')      
api.add_resource(Store, '/store/<string:name>')      
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')



app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# if __name__ == '_main_':

# class User(Resource):

#     @jwt_required()
#     def get(self):   # view all users
#         user = current_identity
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) 
