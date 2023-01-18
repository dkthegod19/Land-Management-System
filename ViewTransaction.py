# This function asks transaction ID from the user and prints the corresponding transaction details

def viewTransaction( blockchain ):
    if len(blockchain.chain)==0: 
        print('\nBlockchain empty!!!')
        return

    quote_string = "\nDetails of Transaction {}::==\nBuyer Name       :  {}\nSeller Name       :  {}\nAmount              :  INR {}\nProperty Name       :  {}\nTimestamp           :  {}"

    while True:
        transaction_id = input("\nEnter Transaction id: ")

        isValid = [False]
        for block in blockchain.chain:
            for transaction in block["transactions_list"]:
                if transaction[0]==transaction_id:
                    isValid = [True, transaction[2], transaction[3], transaction[1], transaction[4], transaction[5]]
                    break
            if isValid[0]: break
                
        if isValid[0]:
            print(quote_string.format(transaction_id, isValid[1], isValid[2], isValid[3],isValid[4],isValid[5]))
        else:
            print("\nInvalid Transaction id!!!")
            YesOrNo = input("\n Execute the same query? [y/n]")
            if YesOrNo =="y":
                continue

        break 
    print("")
    return