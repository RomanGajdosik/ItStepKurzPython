import json

krajiny={"Japan": "Tokyo",
        "Slovakia": "Bratislava",
        "Australia": "Canberra",
        "United States": "Washington, D.C.",
        "Canada": "Ottawa",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Brazil": "Brasília",
        "India": "New Delhi"}


def to_Json(data):
    with open ('dict1','w') as filehandler:
        json.dump(data,filehandler)   

to_Json(krajiny)

def unpack():
    with open('dict1','r') as filehandler:
        dict_unpacked = json.load(filehandler)
        return dict_unpacked 

def add_dict(country,cappital):
    krajiny = unpack()
    krajiny[country]=cappital
    to_Json(krajiny)

def remove_dict(data):
    krajiny = unpack()
    krajiny.pop(data)
    to_Json(krajiny)

def find_dict(data):
     krajiny = unpack()
     hladane_data = krajiny.setdefault(data,'Nenajdene')
     print(hladane_data)
def modify_dict(newkey,newval):
    krajiny = unpack()
    krajiny.update({newkey:newval})
    to_Json(krajiny)

def read():
    data = unpack()
    print(data)

add_dict('OZ','buhvikde')
remove_dict('OZ')
find_dict('OZ')
modify_dict('Atlantida','Netusim')
read()
