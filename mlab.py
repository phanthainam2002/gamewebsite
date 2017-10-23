import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds013495.mlab.com:13495/clowngame
host = "ds013495.mlab.com"
port = 13495
db_name = "clowngame"
user_name = "nam"
password = "nam"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
