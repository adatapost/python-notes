def is_open(data, bit_position):
    '''Returns True or False based upon bit status'''
    return data & (2 ** (bit_position-1)) != 0

def set(data, bit_position):
    return data | (2 ** (bit_position-1))

def unset(data, bit_position):
    if is_open(data, bit_position):
      return data ^ (2 ** (bit_position-1))
    return data

print( is_open(0b00001011,1) )
print(is_open(0b10001000, 4))
for i in range(1,9):
    print(i, " => ", is_open(0b10101010,i))

data = 0b0000_0000
data = set(data, 3)
print(data, bin(data))
data = set(data, 8)
print(data, bin(data))
data = unset(data, 3)
print(data, bin(data))

