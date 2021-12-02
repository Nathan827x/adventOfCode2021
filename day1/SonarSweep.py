

'''
Get a list of the inpuits from a txt file
Go through and make sure they are strings
    While going through and converting to string, compare with the last number
        If the current number is GREATER than the last number, result += 1
        else nothing. Replace the "last num" with the current num and continue

'''

def main():

    depths = createListFromInputs()

    return getTotalTimesDepthIncreases(depths)

def getTotalTimesDepthIncreases(depths):

    depths_increases_from_previous = 0
    last_depth = None

    for depth in depths:

        curr_num = int(depth[:-1])

        if last_depth is None:
            last_depth = curr_num

        elif curr_num > last_depth:
            depths_increases_from_previous += 1
            last_depth = curr_num
        else:
            last_depth = curr_num

    return depths_increases_from_previous
        # # This removes all the "\n" chars
        # print (depth[:-1])



def createListFromInputs():
    f = open('input1.txt', 'r')
    depths = f.readlines()
    return depths



if __name__ == "__main__":
    print(main())