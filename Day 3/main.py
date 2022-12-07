from Util.file_reader import get_lines
import string


def main():
    file = open("input.txt")
    lines = get_lines(file)
    file.close()
    priority_sum_task1 = 0
    priority_sum_task2 = 0
    for line in lines:
        items1, items2 = line[:len(line)//2], line[len(line)//2:]
        common_item_task1 = get_common_item_task1(items1, items2)
        priority_sum_task1 += string.ascii_letters.index(common_item_task1) + 1
    print("Priority sum task 1:", priority_sum_task1)

    x = 0
    while x < len(lines):
        common_item_task2 = get_common_item_task2(lines[x], lines[x+1], lines[x+2])
        priority_sum_task2 += string.ascii_letters.index(common_item_task2) + 1
        x += 3
    print("Priority sum task 2:", priority_sum_task2)


def get_common_item_task1(items1, items2):
    for x in items1:
        for y in items2:
            if x == y:
                return x


def get_common_item_task2(line1, line2, line3):
    for x in line1:
        for y in line2:
            for z in line3:
                if x == y == z:
                    return x


if __name__ == '__main__':
    main()