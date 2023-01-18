# Facilitates separation of data in a transaction
def addSpaces( input, total_length ):
    input = str( input )
    while total_length > len(input):
        input = input + " "
    return input

# This function prints all the verified transactions in the blockchain
def viewTransactions( blockchain ):

    if len(blockchain.chain) == 0:
        print("\nNo completed transactions to display!!!")
        return

    print("Transaction ID      Buyer Name      Seller Name      Amount      Property Name      Timestamp")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    transaction_quote = "{}      {}      {}      {}      {}      {}"

    for block in blockchain.chain:
        for transaction in block['transactions_list']:
            print(transaction_quote.format(
                                        addSpaces(transaction[0], len("Transaction ID")), 
                                        addSpaces(transaction[2], len("Buyer Name")), 
                                        addSpaces(transaction[3], len("Seller Name")),
                                        addSpaces(transaction[1], len("Amount")),
                                        addSpaces(transaction[4], len("Property Name")),  
                                        transaction[5]
                                    ))