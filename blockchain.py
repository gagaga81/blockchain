import hashlib
import json
import time

# ハッシュを計算する関数
def calculate_hash(block):

    # 辞書型を文字列型に変換→JSON
    block_jason = json.dumps(block)

    # encode: unicodeをバイト型に変換
    # SHA256というハッシュ関数でハッシュにし、hexdigestで16進数にする
    return hashlib.sha256(block_jason.encode()).hexdigest()

# print(calculate_hash("gaisho81"))
# #ea7f6eda0976ec081e7369e4b425f5891103cc03a387baeaa6b770b9b383bb10


# ジェネシスブロックの生成
class Genesis:
    def __init__(self):
        self.chain = []
        self.current_transaction = []
        self.transaction_index = 0
        self.create_block(nonce="hoge", previous_hash="0000000000000000000000000000000000000000000000000000000000000000")

        self.current_transaction = []
        self.transaction_index = 0

    def create_block(self, nonce, previous_hash):
        block = {
            'index' : len(self.chain),
            'timestamp' : time.time(),
            'transactions' : self.current_transaction,
            'nonce' : nonce,
            'previous_hash' : previous_hash
        }
        self.chain.append(block)

        return block

# print(Genesis().chain)

