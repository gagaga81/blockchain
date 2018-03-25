import hashlib

def cal(string):
    nonce = 0
    while True:
        block = string + str(nonce)

        hblock = hashlib.sha256(block.encode()).hexdigest()

        if hblock[:1] == "0":
            break

        nonce +=1

    return block

print(cal("gaisho"))