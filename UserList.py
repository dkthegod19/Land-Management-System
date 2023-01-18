from asyncio.windows_events import NULL
users = []  # List to store the users along with the properties they own(if any)
properties = [] # List to store all the properties along with the owner name and its transaction history
def addUser():
    while True:
        username = input('Enter username  ')
        for user in users:
            if(username == user["name"]):
                print('User already exists, try again')
                return NULL
        prop = 'null'
        hasprop = input('Does the user own any property? [y/n]  ')
        if(hasprop == 'y'):
            prop = input('Enter property name  ')   
            property = {
                "name": prop,
                "owner": username,
                "history": [],
            }
            properties.append(property)
            user = {
                "name": username,
                "ownedprop": []
            }
            user['ownedprop'].append(prop)
        else:
            user = {
                "name":username,
                "ownedprop":[]
            }    
        users.append(user)
        yesOrno = input('Execute same query? [y/n]  ')
        if yesOrno == 'y':
            continue
        else:
            break;     
          