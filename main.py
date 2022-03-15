# main file

import sys
import math
#import moves # local

_PFORMAT = "Usage: main.py <EETAS file>"# [-s]"
_MOVES = ['J', '←', '→', '↑', '↓']

#_FLAG_SHORT = False

# convert ASCII character to move id
def ctom(c):
    if ord(c) < 48 or ord(c) > 79:
        return -1
    return ord(c) - 48

# format line in string
def build_line(align, total, move, counter):
    move_string = ""
    
    # check if a particular bit is 1
    for i in range(5):
        if move & 2**i:
            move_string += _MOVES[i]
        else:
            move_string += " "
        move_string += " "

    ret = "{}".format(total).rjust(align)
    ret += " | "
    ret += "{} | {}\n".format(move_string, counter)
    return ret 

# construct the output string
def build_string(file):
    # count how many characters are in the file
    #  used for determining align width for total tick count
    tick_align = math.log10(len(file.read()))
    tick_align = math.ceil(tick_align)
    file.seek(0, 0)

    ret = ""
    curr_char = file.read(1)
    total_ticks = 0
    counter = 1
    while True:
        char = file.read(1)
        if not char:
            break
        if char == curr_char:
            counter += 1
        else:
            move = ctom(char)
            if move == -1:
                continue
            total_ticks += counter
            ret += build_line(tick_align, total_ticks, move, counter)
            curr_char = char
            counter = 1
    file.close()

    return ret

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("ERROR: Incorrect number of parameters")
        print(_PFORMAT)
        quit()

    # check if "short move names" option is chosen
    #if len(sys.argv) > 2 and sys.argv[2] == "-s":
    #    _FLAG_SHORT = True

    file = open(sys.argv[1], 'r')
    string = build_string(file)
    print(string)
