from Util.file_reader import get_lines
from collections import Counter
import re


def main():
    file = open("input.txt")
    line = file.readline()
    task1 = get_index(line, 4)
    task2 = get_index(line, 14)

    print("Task 1: ", task1)
    print("Task 2: ", task2)


def get_index(line, req_len):
    x = 0
    while x + req_len < len(line):
        if len(Counter(line[x:x + req_len])) == len(line[x:x + req_len]):
            print("Answer: ", line[x:x + req_len], "Index: ", x + req_len)
            return x + req_len
        x += 1
    return -1


if __name__ == '__main__':
    main()
