# Code generate function
def generate_roll(no):
    return "AF" + (4 - len( str(no) )) * "0" + str(no)

print( generate_roll(403), generate_roll(20))
    

