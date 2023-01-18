# Calculating the hash in order to add digital fingerprints to the blocks
import hashlib
import json
import UserList
class Blockchain:
   
    # This function initialises the blockchain
    # It stores the chain in the form of a tuple which is immutable
    def __init__(self):
        self.chain = ()
 
    # This function adds the blocks into the chain.
    def create_block(self, previous_hash, nonce, tx_list,merkleroot):
        block = {'index': len(self.chain) + 1,
                 'merkleroot' : merkleroot,
                 'previous_hash': previous_hash,
                 'proof': nonce,
                 'transactions_list': tx_list
                 }
        temp_list = list(self.chain)
        temp_list.append( block )
        self.chain = tuple(temp_list)
        return block
       
    # This function gets the last added block
    def latest_block(self):
        return self.chain[-1]

    #This function uses SHA256 hashing algorithm to create the merkle root from the transactions of a block
    def hash(self, transactions):    
        tx1 = json.dumps(transactions[0]).encode()
        tx2 = json.dumps(transactions[1]).encode()
        tx3 = json.dumps(transactions[2]).encode()
        tx1 = hashlib.sha256(tx1).hexdigest()
        tx2 = hashlib.sha256(tx2).hexdigest()
        tx3 = hashlib.sha256(tx3).hexdigest()
        tx12 = tx1 + tx2
        tx33 = tx3 + tx3
        tx12 = hashlib.sha256(tx12.encode()).hexdigest()
        tx33 = hashlib.sha256(tx33.encode()).hexdigest()
        merkleroot = tx12 + tx33
        merkleroot = hashlib.sha256(merkleroot.encode()).hexdigest()
        return merkleroot
    
    # proof of work algorithm is implemented here
    def proof_of_work(self, previous_proof):
        nonce = 1
        is_proof_valid = False
         
        while is_proof_valid is False:
            hash_operation = hashlib.sha256(
                (str(nonce*2) + str(previous_proof*2)).encode()).hexdigest()
            if hash_operation[:2] == '00':
                is_proof_valid = True
            else:
                nonce += 1
                 
        return nonce

    #This function mines the block
    def mine_block(self, tx_list):
        if len(self.chain)==0:
            genesisBlock = hashlib.sha256('GenesisBlock'.encode()).hexdigest()
            previous_hash = genesisBlock
        else:
            previous_block = self.latest_block()
            previous_hash = hashlib.sha256(json.dumps(previous_block).encode()).hexdigest()  #Merkle root should be added here
        
        if len(self.chain)==0:
            nonce = 1
        else:
            nonce = self.proof_of_work( self.latest_block()['proof'] )
        currmerkleroot = self.hash(tx_list)
        self.create_block(previous_hash, nonce, tx_list,currmerkleroot)


    #This function updates the transaction history related to a property 
    def updatePropHistory(self,transaction):
               prop_in_tx = transaction[4]
               for prop in UserList.properties:
                   if(prop['name'] == prop_in_tx):
                      prop['history'].append(transaction)
                                           
                      
    #This function updates the owners of a property after the transactions           
    def updateOwners(self,tx):
        seller = tx[3]
        buyer = tx[2]
        property = tx[4]
        for user in UserList.users:
            if user['name'] == seller:
                if user['ownedprop'].count(property):
                    user['ownedprop'].remove(property)
                    break
                
        #adding property to buyer's properties
        for user in UserList.users:
                if user['name'] == buyer:
                    user['ownedprop'].append(property)
                    break
                            
        #updating current owner in properties
        for prop in UserList.properties:
            if  prop['name'] == property:
                prop.update({'owner':buyer})
                break       
                   
                       