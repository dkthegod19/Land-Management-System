#This function prints the unverified transactions
from ViewVerifiedTransactions import addSpaces


def viewUnverifiedTransactions( leftover_transactions ):
    if len(leftover_transactions) == 0: 
            print("\n All transactions are verified")
            return

    print("Transaction ID      Buyer Name      Seller Name      Amount      Property Name      Timestamp")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    
    for unverified_trn in leftover_transactions:
        print("{}      {}      {}      {}      {}      {}".format(
            addSpaces(unverified_trn[0], len("Transaction ID")), 
            addSpaces(unverified_trn[2], len("Buyer Name")), 
            addSpaces(unverified_trn[3], len("Seller Name")),
            addSpaces(unverified_trn[1], len("Amount")),
            addSpaces(unverified_trn[4], len("Property Name")), 
            unverified_trn[5]
        ))