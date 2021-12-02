

'''
Get a list of the inpuits from a txt file
Go through and make sure they are strings
    While going through and converting to string, compare with the last number
        If the current number is GREATER than the last number, result += 1
        else nothing. Replace the "last num" with the current num and continue

So now we have to take extra things into account...
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H

Start by comparing the first and second three-measurement windows. 
The measurements in the first window are marked A (199, 200, 208); 
their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); 
its sum is 618. The sum of measurements in the second window is 
larger than the sum of the first, so this first comparison increased.

NEW SOLUTION:
So I am thinking what they mean is that, we collect the numbers in batches of 3 to check the depths.
So 199 + 200 + 208
200 + 208 + 210
208 + 210 + 200

# KEEP THIS IN MIND
It also seems that once we hit the last windows (269 + 260 + 263)
we need to stop the interation. I guess it doesn't matter if we stop since 
the sum  of 2 or less numbers will not likely be bigger than the previous window
'''

def main():
    depths = createListFromInputs()
    num_depths = convertStringListToInt(depths)

    print("The total depths increased part 1: ", getTotalTimesDepthIncreases(num_depths))
    print("The total depths with a window of 3 increased part 2: ", solvingDepthByWindowDepth(num_depths))

def convertStringListToInt(depths):
    res = []

    for each in depths:
        res.append(convertStringToInt(each))
    return res


def solvingDepthByWindowDepth(depths):
    total_depths = createWindowFromDepths(depths)
    return getTotalTimesDepthIncreases(total_depths)


def createWindowFromDepths(depths):    
    res = []
    depth_counter = 0

    # Create 1 window, that looks 2 ahead for a total of 3 spaces.
    # Iterate to EVERY number while looking ahead 2.
    while depth_counter < len(depths) - 2:
        
        first_depth, second_depth, third_depth = depths[depth_counter], depths[depth_counter + 1], depths[depth_counter + 2]
        res.append(first_depth + second_depth + third_depth)
        depth_counter += 1
    
    return res


def convertStringToInt(str_num):
    return int(str_num[:-1])


def getTotalTimesDepthIncreases(depths):
    depths_increases_from_previous = 0
    last_depth = None

    for depth in depths:
        
        if last_depth is None:
            last_depth = depth

        elif depth > last_depth:
            depths_increases_from_previous += 1
            last_depth = depth
            
        else:
            last_depth = depth

    return depths_increases_from_previous


def createListFromInputs():
    f = open('input1.txt', 'r')
    depths = f.readlines()
    return depths


if __name__ == "__main__":
    main()