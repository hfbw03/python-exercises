# Count the number of cubes with paint on
# https://www.codewars.com/kata/5763bb0af716cad8fb000580

'''
Upon arriving at an interview, you are presented with a solid blue cube. The cube is then dipped in 
red paint, coating the entire surface of the cube. The interviewer then proceeds to cut through the 
cube in all three dimensions a certain number of times. Your function takes as parameter the number 
of times the cube has been cut. You must return the number of smaller cubes created by the cuts that 
have at least one red face.
'''

def paintedCube(cuts):
    # An edge case because the formula below doesn't work for 0.
    if cuts == 0:
        return(1)
    elif cuts < 0:
        return("Please input a nonnegative integer")
    else:
        return(((cuts + 1) ** 3) - ((cuts - 1) ** 3))

paintedCube(5)