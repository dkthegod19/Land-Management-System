import json

def viewBlock( blockchain ):
    if len(blockchain.chain)==0:
        print("\nNo blocks available in blockchain")
        return
    
    while True:
        while True:
            try:
                index = int(input("\n Specify Block Index: "))
                break
            except ValueError:
                print("\n Invalid Value, please try again")
                continue

        if index > len(blockchain.chain):
            print("\n Invalid Index ")
            yesORno = input("\n Repeat the request[y/n]")
            if yesORno == 'y':
                continue
        break

    for block in blockchain.chain:
        if block["index"]==index:
            print(json.dumps(block, indent=4))
            return
    
    print("\n Block not found! ")
    return

# This function prints the entire blockchain
def viewBlockchain( blockchain ):
    if len(blockchain.chain) == 0:
        print("\n Chain Length is zero, no Blocks added ")
        return
    
    print(json.dumps(blockchain.chain, indent=5))