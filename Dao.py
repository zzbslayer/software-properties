from mongoengine import Document, connect, StringField, IntField, ListField
import Util

db_db = "sjtu_center"
db_host = "localhost"
connect(db=db_db, host=db_host)

class Server(Document):
    domain = StringField(required=True)
    web_port = StringField(required=True)
    software = StringField(required=True)