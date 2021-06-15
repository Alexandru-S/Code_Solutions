import sys

super_stack = []  # super stack list tracker

for line in sys.stdin:
    if (" " in line) == True:
        command_list = line.split(" ")
        if command_list[0] == "push":  # push operation, using python insert
            super_stack.insert(0, (int(command_list[1])))
            print(super_stack[0])

        if (
            command_list[0] == "inc"
        ):  # inc operation, using slice notation to append from bottom up
            for x in range(int(command_list[1])):
                inc = -(x + 1)
                super_stack[inc] += int(command_list[2])
            print(super_stack[0])
    else:
        if "pop" in line:  # pop operation, using python pop
            super_stack.pop(0)
            if len(super_stack) >= 1:
                print(super_stack[0])
            else:
                print("EMPTY")


###################################################################################################################
import sys


# time complexity O(n) worst case
def superStack(input_array):
    """
    The same exercise as above but in function format that can accept
    an array given to its
    Args:
        input_array (list): A list of instruction strings that can perform
                            push, pop or addition actions on the stack

    """
    super_stack = []  # super stack list tracker
    for line in input_array:
        if (" " in line) == True:
            command_list = line.split(" ")
            if command_list[0] == "push":  # push operation, using python insert
                super_stack.insert(0, (int(command_list[1])))
                print(super_stack[0])

            if (
                command_list[0] == "inc"
            ):  # inc operation, using slice notation to append from bottom up
                for x in range(int(command_list[1])):
                    inc = -(x + 1)
                    super_stack[inc] += int(command_list[2])
                print(super_stack[0])
        else:
            if "pop" in line:  # pop operation, using python pop
                super_stack.pop(0)
                if len(super_stack) >= 1:
                    print(super_stack[0])
                else:
                    print("EMPTY")
