# This function prints the time when this transaction was completed.
def viewTimestamp( blockchain ):
    if len(blockchain.chain) == 0: 
        print('\nBlockchain is currently empty')
        return

    quote_string = "\nTHE TRANSACTION WAS COMPLETED ON {}"

    while True:
        transaction_id = input("\nEnter Transaction id: ")

        isValid = [False]
        for block in blockchain.chain:
            for transaction in block["transactions_list"]:
                if transaction[0]==transaction_id:
                    isValid = [True, transaction[5]]
                    break
            if isValid[0]: break
        
        if isValid[0]:
            print( quote_string.format(isValid[1]) )
        else:
            print("\n Transaction ID Invalid")
            yesORno = input("\n Execute the same query? [y/n]")
            if yesORno=="y":
                continue

        break
    
    print("")
    return