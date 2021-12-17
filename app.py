from mongoengine import connect
import mongoengine
from mongoengine.errors import NotUniqueError
from orm.user import User

connect(
    db='project1',
    host='localhost',
    port=27017,
    username='',
    password='',
    authentication_source='admin'
)

try:
    user = User(email='test@email.com')
    user.first_name = 'bruno'
    user.last_name = 'alves'
    user.save()
except NotUniqueError as e:
    print('Email is already found')
