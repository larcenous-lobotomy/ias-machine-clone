#a list of function declarations for supporting implementation

#num is an unsigned binary string
def unsign_to_dec(num):
    return int(num,2)

#num is a signed binary string
def sign_to_dec(num):
    return (1 if num[0] == "0" else -1)*int(num[1:],2)

#decimal to signed binary of length 40 - a word for storage into memory
def dec_to_sign(num):
    return "0"*(40 - len(bin(num)[2:])) + (bin(num)[2:]) if (num>0) else "1" + "0"*(40 - len(bin(num)[3:]) - 1) + (bin(num)[3:])

def dec_to_unsign(num):
    return "0"*(40 - len(bin(num)[2:])) + (bin(num)[2:])