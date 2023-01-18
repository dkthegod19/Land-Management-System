import UserList
import json

print_string ="\n {} \n Properties Owned: {} \n"
#this function prints the properties owned by each user
def pri():
    for user in UserList.users:
        print(print_string.format(json.dumps(user['name'],indent = 3),json.dumps(user['ownedprop'],indent=3)))

#this function shows the transactions related to a property
def history(property):
    for prop in UserList.properties:
        if(prop['name']==property):
            print(json.dumps(prop['history'],indent=3))
        
