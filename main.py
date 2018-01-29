from algo import bitstuffing, bytestuffing

def bit_stuffing():
    inp = input("Enter bits: ")
    print("Final bits are {}".format(bitstuffing.stuff_bit(bitstuffing.to_bitarray(inp)).bin))

def byte_stuffing():
    inp = input("Enter character stream: ")
    print("Final stream is {}".format(bytestuffing.stuff_byte(inp)))
    print("FLAG = 'F'")
    print("ESC = '/'")

# byte_stuffing()