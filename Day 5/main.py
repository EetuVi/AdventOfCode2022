from Util.file_reader import get_lines
import re


def main():
    file = open("input.txt")
    lines = file.readlines()
    columns = get_columns(lines)
    columns2 = columns.copy()

    final_columns = make_moves(columns, lines)
    final_columns_task2 = make_moves(columns2, lines, False)

    top_crates = ""
    top_crates_task2 = ""

    for col in final_columns:
        top_crates += col[-1:][0]

    for col in final_columns_task2:
        top_crates_task2 += col[-1:][0]

    print("Top crates task 1: ", top_crates)
    print("Top crates task 2: ", top_crates_task2)


def get_columns(lines):
    columns = []
    cols = list()
    for line in lines:
        if line.strip().replace(" ", "").isdigit():
            cols = int(line.strip().replace(" ", "")[-1])

    x = 0
    while x < cols:
        columns.append([])
        x += 1
    populated_columns = populate_columns(columns, lines)
    return populated_columns


def populate_columns(columns, lines):
    x = 0
    y = 0
    for line in lines:
        x = 1
        y = 0
        if line[x] == "1":
            break
        while x < len(line):
            if line[x] != " ":
                columns[y].append(line[x])
            if (x + 5) > len(line):
                break
            x += 4
            y += 1
    for col in columns:
        col.reverse()
    return columns


def make_moves(columns, lines, reverse = True):
    moves = False
    for line in lines:
        if len(line) == 1:
            moves = True
            continue
        if moves:
            orders = line.split()
            moving_crates = columns[int(orders[3])-1][-int(orders[1]):]
            if reverse:
                moving_crates.reverse()
            remaining_stack = columns[int(orders[3])-1][:-int(orders[1])]
            for crate in moving_crates:
                columns[int(orders[5])-1].append(crate)
            columns[int(orders[3])-1] = remaining_stack

    return columns


if __name__ == '__main__':
    main()
