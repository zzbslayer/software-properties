from mongoengine import Document, connect, StringField, IntField, ListField
import Util

db_db = "sjtu"
db_host = "localhost"
connect(db=db_db, host=db_host)

class Server(Document):
    domain = StringField(required=True)
    port = StringField(required=True)
    software = StringField(required=True)
    lic = StringField(required=True)

class History(Document):
    server_id = IntField(required=True)
    software = StringField(required=True)
    module = StringField(required=True)
    date = StringField(required=True)
    time = StringField(required=True)
    total = IntField(required=True)
    use = IntField(required=True)
    metadata = ListField()
    user_data = ListField()