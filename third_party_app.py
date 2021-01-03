import requests
import json

URL= "http://127.0.0.1:8000/student_api"

def getdata(id=None):
    data={}
    if id is not None:
        data= {'id':id}
    json_data= json.dumps(data)
    headers= {'content-Type':'application/json'}
    r= requests.get(url=URL, headers=headers, data=json_data)
    data= r.json()
    print(data)

getdata()

def postdata():
    data={
        'name':'Hary',
        'roll':123,
        'city':'ramput'
    }

    json_data= json.dumps(data)
    headers= {'content-Type': 'application/json'}
    r= requests.post(url= URL, headers=headers, data=json_data)
    data= r.json()
    print(data)

# postdata()

def updatedata():
    data={
        'id': 1,
        'name':'sumitbro123',
        'roll':123,
        'city':'rampur'
    }

    json_data= json.dumps(data)
    headers={'content-Type': 'application/json'}
    r= requests.put(url= URL, headers= headers, data=json_data)
    data= r.json()
    print(data)

# updatedata()


def deletedata():
    data={
        'id': 1
        
    }

    json_data= json.dumps(data)
    headers={'content-Type': 'application/json'}
    r= requests.delete(url= URL, headers= headers, data=json_data)
    data= r.json()
    print(data)

# deletedata()