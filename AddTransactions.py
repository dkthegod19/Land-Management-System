import datetime
import UserList
import BlockChain

blockchain = BlockChain.Blockchain()
#function for accepting input by the user from the terminal
def inputTransactions( blockchain, leftover_trns ):

    input_transactions = leftover_trns
   
    while True:
        print("\nInput Transaction details")

        while True:
            trn_id = input("\n Input Transaction id : ")

            exists = False
            for block in blockchain.chain:
                for transaction in block["transactions_list"]:
                    if trn_id == transaction[0]:
                        exists = True
                        break
                if exists: break
            for transaction in input_transactions:
                if exists: break
                else:
                    if trn_id == transaction[0]:
                        exists = True
                        break
            if exists: 
                print("\nTransaction already exists! Please Try again.")
                continue
            break

        amount = -1
        while True:
            try:
                amount = float(input("\n Enter The Amount         : "))
                break
            except ValueError:
                print("\nInvalid amount!! Please try again")
        
        buyer_name = input("\n>>> Buyer Name  : ") 
        flag1 = 0
        for user in UserList.users:
            if(user['name'] == buyer_name):
                flag1 = 1
                break
        if(flag1==0):
            print('User not registered, please register and try again')
            break
                       
        property_name= input("\nEnter Property Name : ") 
        #an array containing properties will be constructed
        flag = 0
        for property in UserList.properties:
            if(property['name'] == property_name):
                seller_name = property['owner']
                flag = 1
                break
        if(flag == 0):
            print('Property does not exist!')
            break     
        #buyers and sellers names will be registered
        #list of all buyers and sellers are contained in users in UserList
        # along with registering everyone we need to check if a property is bought or unsold yet
        input_transactions.append((
            trn_id,  #0
            amount,  #1
            buyer_name, #2
            seller_name, #3
            property_name, #4 
            str(datetime.datetime.now().strftime("%Y-%m-%d AT %H:%M %p")) 
        ))
        # After a transaction is initiated, the names of the buyer and seller are interchanged
        blockchain.updateOwners(input_transactions[-1])
        # That Transaction is added to the property's history
        blockchain.updatePropHistory(input_transactions[-1])
        y_or_n = input("\nD O N E!\n Do You Want To Add more?[y/n]")

        if y_or_n == 'n':
            return input_transactions


#the below function will verify the transactions and if there is atleast 3 transactions it will add them to the block
def addTransactions( input_transactions, blockchain ):
    if input_transactions is None:
        return []
    count = len(input_transactions)
    while count>=3:
        verified_trn_list = tuple(input_transactions[:3])
        input_transactions = input_transactions[3:]

        blockchain.mine_block( verified_trn_list )

        count = count-3

    return input_transactions
    