import BlockChain
import AddTransactions
import ViewTransaction
import ViewVerifiedTransactions
import ViewTransactionTimestamp
import ViewBlockchain
import ViewUnverifiedTransactions
import UserList
import ViewPropTransactionHistory
blockchain = BlockChain.Blockchain()    # Starting the blockchain

remaining_trns = [] 
while True:
    print("\n*****************************************")
    print('           Land Management System          ')
    print("*******************************************")
    print("\n[0] - Register a User")
    print("[1] - Add a Transaction")
    print("[2] - View the Blockchain")
    print("[3] - View Verified Transactions")
    print("[4] - View Unverified Transactions")
    print("[5] - Print Property Transaction History")
    print("[6] - Print Users")
    print("[7] - View a Transaction")
    print("[8] - View a block")
    print("[9] - View Timestamp of a transaction")
    print("\n[e] - Exit Program")
    option = input("\nChoose an option:  ")

    if option == "0":
        UserList.addUser()

    elif option == "1": 
        unverified_trns = AddTransactions.inputTransactions( blockchain, remaining_trns )
        remaining_trns = AddTransactions.addTransactions( unverified_trns, blockchain )
        # Three transactions make a block, difference between
        # the total transactions and the nearest multiple of three make up the unverified transactions.
    
    elif option == "2":
        ViewBlockchain.viewBlockchain(blockchain)
        
    elif option == "3":
        ViewVerifiedTransactions.viewTransactions(blockchain)
    
    elif option == "4":         
        ViewUnverifiedTransactions.viewUnverifiedTransactions(remaining_trns)
    
    elif option == "5":
        property=input('Enter the Property name ')         
        ViewPropTransactionHistory.history(property)
    
    elif option == "6":         
        ViewPropTransactionHistory.pri()

    elif option == "7":
        ViewTransaction.viewTransaction(blockchain)

    elif option == "8":
        ViewBlockchain.viewBlock(blockchain)

    elif option == "9":
        ViewTransactionTimestamp.viewTimestamp(blockchain)

    elif option == "e":
        print('Exiting Program....')
        print("\nThankyou For using our LMS!!!")
        break

    else:
        print('Unrecognized input, please try again')