from hashlib import sha256
from time import ctime


class Block(object):
    def __init__(self, index, parent_hash, timestamp, transactions):
        super().__init__()
        self.index = index
        self.parent_hash = parent_hash
        self.timestamp = timestamp
        self.nonce = 0
        self.transactions = transactions

    def hash(self):
        print("Mining... Index: {}, Nonce: {}".format(self.index,self.nonce))
        return sha256((str(self.index)+str(self.parent_hash)+str(self.timestamp)+str(self.transactions)+str(self.nonce)).encode()).hexdigest()

    def set_hash(self):
        self.hash_value = self.hash()
    
    def __repr__(self):
        return "Block: {}, {} \n Timestamp: {} \n Transactions: {}".format(self.index, self.hash_value,self.timestamp,self.transactions)



class Blockchain(object):
    def __init__(self):
        super().__init__()
        
        self.difficulty = 3
        self.unconfirmed_transactions = []
        self.chain = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        self.genesis = Block(0,"0"*64,ctime(),[])
        while not self.genesis.hash().startswith("0"*self.difficulty):
            self.genesis.nonce=1+self.genesis.nonce
        self.genesis.set_hash()
        self.chain.append(self.genesis)
        return self.chain[-1].index

        
    def addTransaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)


    def mine(self):
        new_block = Block(self.chain[-1].index+1,self.chain[-1].hash(),ctime(),self.unconfirmed_transactions)
        self.unconfirmed_transactions = []

        while not new_block.hash().startswith("0"*self.difficulty):
            new_block.nonce+=1
        new_block.set_hash()
        self.chain.append(new_block)
        return self.chain[-1].index
    
    def __repr__(self):
        for block in self.chain:
            print(block)
        return super().__repr__()

myBlockchain = Blockchain()
for i in range(20):
    myBlockchain.addTransaction("I send you £{}".format(i))
myBlockchain.mine()

for i in range(5):
    myBlockchain.addTransaction("I send you £{}".format(i))
myBlockchain.mine()

print(myBlockchain)
