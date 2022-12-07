from Util.file_reader import get_lines


def main():
    file = open("test.txt")
    lines = file.readlines()
    columns = []
    for line in lines:
        if line.strip().replace(" ", "").isdigit():
            cols = int(line.strip().replace(" ", "")[-1])

    x = 0
    while x < cols:
        columns.append([])
        x+=1
    print(columns)

    x = 0
    y = 0
    for line in lines:
        x = 1
        y = 0
        if line[x] == "1":
            break
        while x < len(line):
            if line[x] == "":
                columns[y].append("0")
            else:
                columns[y].append(line[x])
            if (x + 5) < len(line):
                x += 4
                y += 1
    print(columns)

if __name__ == '__main__':
    main()