import requests
import json

URL= "http://127.0.0.1:8000/student_api"

def getdata(id=None):
    data={}
    if id is not None:
        data= {'id':id}
    json_data= json.dumps(data)
    r= requests.get(url=URL, data=json_data)
    data= r.json()
    print(data)

# getdata()

def postdata():
    data={
        'name':'sumit',
        'roll':123,
        'city':'ramput'
    }

    json_data= json.dumps(data)
    r= requests.post(url= URL, data=json_data)
    data= r.json()
    print(data)

# postdata()

def updatedata():
    data={
        'id': 2,
        'name':'sumitbro',
        'roll':123,
        'city':'rampur'
    }

    json_data= json.dumps(data)
    r= requests.put(url= URL, data=json_data)
    data= r.json()
    print(data)

# updatedata()


def deletedata():
    data={
        'id': 2
        
    }

    json_data= json.dumps(data)
    r= requests.delete(url= URL, data=json_data)
    data= r.json()
    print(data)

deletedata()