'''
PROBLEM/Ideas:
It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.


Your horizontal position and depth both start at 0. The steps above would then modify them as follows:
    
Keep track of horizontal (foward)
and vertical (down is + and up is -)

Once you get those numbers multiply and return the solution.
'''

'''
I'm wondering if it can go negative (Above the water) So like moving up 10 times and then stopping

I think I should be able to do this in one loop where I read the lines, keeping track of the forward,
up, and down movement. Then, I just multiply the solution

PART 2:
down X increases your aim by X units.
up X decreases your aim by X units.

ex:
    forward 3, aim = 0
    forward = 3+5, aim = 3
    forward = 3+5+1, aim = 8

Then you just have to multiply for a new depth
    depth = depth + aim * Forward movement in that instance. If you follow the same example values above.
    depth = depth + 0 * 3
    depth = depth + 3 * 5
    depth = depth + 8 * 1
    depth = aim * movment
'''

'''
If I want to keep it clean, I think I would need to utilize classes.
'''


def main():

    # first_solution, second_solution = findLocationOfSubmarine()

    print("Part 1 solution: ", findLocationOfSubmarineWithoutAim())
    print("Part 2 solution: ", findLocationOfSubmarineWithAim())

def findLocationOfSubmarineWithAim():

    forward = 0
    depth = 0
    aim = 0
    file_input = open("directions.txt", 'r')

    for command in file_input:

        direction, movement = command.split()
        direction = direction.lower()
        movement = int(movement)

        if direction == "forward":

            forward += movement
            depth += aim * movement

        elif direction == "up":

            # depth -= movement
            aim -= movement

        elif direction == "down":

            # depth += movement
            aim += movement

        else:
            print("I think something messed up :(")

    return forward * depth

def findLocationOfSubmarineWithoutAim():

    forward = 0
    depth = 0
    file_input = open("directions.txt", 'r')

    for command in file_input:

        direction, movement = command.split()
        direction = direction.lower()
        movement = int(movement)

        if direction == "forward":
            forward += movement
        elif direction == "up":
            depth -= movement
        elif direction == "down":
            depth += movement
        else:
            print("I think something messed up :(")

    return forward * depth

if __name__ == "__main__":
    main()