'''
Looking for Power Consumption = Gamma rate * Epsilon Rate

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Gamma rate = most common bit in the corresponding position
Gamma rate = 10110 = 22

Epsilon rate = Least Common Bit
Epilon = 01001 = 9

At first glance, I just find one, rate and then inverse that solution to get the other value
then I return the multiplied solution

I would ask something about the inputs being different sizes, like is there a default value? (trailing 0s is bad for binary)
If I wanted to make it so that we could be sure to take ALL sizes, I could iterate from each element backwards, and finding what is most common
    So reading from right to left and having the default comparison value be 0 if there isn't a number? 
    BUT the inputs all seem to be the same size...
What to do if the values 1 and 0 are the same (3 ones and 3 zeros)

Could I do something with math? since it's all binary, I could take a running sum for each position in a hashmap. Then I can divide the total
length of the input array and see if it's more than half the sum. This is a way to get the more common value.

There are 12 inputs. so for the most left value, 5 > 12//2 is FALSE. So that means the most right value is 0
{
    0: 5
    1:
    2:
    3:
}

'''

from typing import final


def main():

    file_input = open("example.txt", 'r')
    raw_input = file_input.read().splitlines()
    total_readings = len(raw_input)

    gamma_rate_binary = getGammaRate(raw_input, total_readings)
    epsolon_rate_binary = getEpsilonRate(gamma_rate_binary)
    print("EPI", int(epsolon_rate_binary, 2))

    print("Part 1 Solution: ", int(gamma_rate_binary, 2) * int(epsolon_rate_binary, 2)) 
    
def getEpsilonRate(gamma_rate):
    print(gamma_rate[::-1])
    return gamma_rate[::-1]

def getGammaRate(raw_input, total_readings):

    total_sum_for_binary = {}

    for binary in raw_input:

        addBinaryToTotalSum(total_sum_for_binary, binary)

    return findMostCommonBinaryValue(total_sum_for_binary, total_readings)


def findMostCommonBinaryValue(total_sum_for_binary, total_readings):

    compare_val = total_readings // 2
    res = ''

    for key, value in total_sum_for_binary.items():
        if value >= compare_val:
            res += '1'
        else:
            res += '0'

    return res
        


def addBinaryToTotalSum(total_sum_for_binary, binary):

    binary_position = 0
    
    while binary_position < len(binary):

        curr_binary_number = int(binary[binary_position])

        if binary_position not in total_sum_for_binary:
            total_sum_for_binary[binary_position] = curr_binary_number
        else:
            total_sum_for_binary[binary_position] += curr_binary_number

        binary_position += 1



if __name__ == "__main__":
    main()