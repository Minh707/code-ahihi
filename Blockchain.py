import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8') 
        )    
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo)

class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    Block = Block("Genesis")
    dummy = head = Block

    def add(self, block):
        block.previous_hash = self.Block.hash()
        block.blockNo = self.Block.blockNo + 1

        self.Block.next = block
        self.Block = self.Block.next


    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

Blockchain = Blockchain()

for n in range(10):
    Blockchain.mine(Block("Block " + str(n+1)))

while Blockchain.head != None:
    print(Blockchain.head)
    Blockchain.head = Blockchain.head.next    

