gate_number = int( input("Enter the gate number ( 1 to 8 "))

gate_data = 0b10000000  # 128 value
#print( gate_data)
#print(2 ** (gate_number-1))

power = 2 ** (gate_number-1)

# print(f"{gate_number} is on") if gate_data & power else print(f"{gate_number} is off")
if gate_data & power:
    print(f"{gate_number} is opened!!!")
else:
    print(f"{gate_number} is closed!!!")
