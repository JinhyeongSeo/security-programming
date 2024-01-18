from Crypto.Hash import SHA512
import time
class Block:
    #필드값
    #생성자
    def __init__(self, index, previous_hash, timestamp, userName, data, nonce = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.nonce = nonce
        self.userName = userName
        self.data = data
        self.hash = self.calculate_Hash()
    # 메소드
    def calculate_Hash(self):
        value = f"{self.index}{self.previous_hash}{self.timestamp}{self.userName}{self.nonce}{self.data}"
        return SHA512.new(value.encode()).hexdigest()

    def get_Hash(self):
        return self.hash
    def get_Value(self):
        return 0

    def set_Value(self, num):
        self.num = num

    def print_Block(self):
        print(f"""
        Block # : {self.index}, Previous_Hash : {self.previous_hash}
        TimeStamp : {self.timestamp}
        Data : {self.data}
        Hash : {self.hash}
        """)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0,0,int(time.time()),"MyBlock","Genesis Block",0)

    def add_block(self, new_Block):
        new_Block.previous_hash = self.get_last_block().hash
        new_Block.hash = new_Block.calculate_hash
        self.chain.append(new_Block)

    def get_last_block(self):
        return self.chain[-1]
def main():
    my_blockchain = Blockchain()

    my_first_block = Block(1, my_blockchain.get_last_block().hash, int(time.time()), "Bob", "Bob's public key", 0)
    my_first_block.print_Block()
    my_second_block = Block(1, my_first_block.get_Hash(), int(time.time()), "Alice", "Alice's public key", 0)
    my_second_block.print_Block()

    my_blockchain.add_block(my_first_block)
    my_blockchain.add_block(my_second_block)

    for block in my_blockchain.chain: # my_blockchain.chain --> self.chain 인 [ ] 리스트...
        if block.userName == "Alice":
            print(f"Alice's public key : {block.data}")

if __name__ == "__main__":
    main()