from Util.file_reader import get_lines
from collections import Counter


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


head_position = Coordinates(0, 0)
tail_position = Coordinates(0, 0)
visited_coordinates = ["00"]


def main():
    global visited_coordinates
    file = open("input.txt")
    lines = get_lines(file, True, " ")
    for line in lines:
        match line[0]:
            case "R":
                move_right(int(line[1]))
            case "L":
                move_left(int(line[1]))
            case "U":
                move_up(int(line[1]))
            case "D":
                move_down(int(line[1]))
    print(len(Counter(visited_coordinates)))


def move_right(moves):
    global head_position
    global tail_position
    global visited_coordinates
    for i in range(moves):
        head_position.x += 1
        if abs(tail_position.y - head_position.y) == 1 and abs(tail_position.x - head_position.x) == 2:
            tail_position.x += 1
            tail_position.y += 1 if tail_position.y - head_position.y == -1 else -1
            visited_coordinates.append(str(tail_position.x) + str(tail_position.y))
        if abs(tail_position.x - head_position.x) == 2:
            tail_position.x += 1
            visited_coordinates.append(str(tail_position.x) + str(tail_position.y))


def move_left(moves):
    global head_position
    global tail_position
    global visited_coordinates
    for i in range(moves):
        head_position.x -= 1
        if abs(tail_position.y - head_position.y) == 1 and abs(tail_position.x - head_position.x) == 2:
            tail_position.x -= 1
            tail_position.y += 1 if tail_position.y - head_position.y == -1 else -1
            visited_coordinates.append(str(tail_position.x) + str(tail_position.y))
        if abs(tail_position.x - head_position.x) == 2:
            tail_position.x -= 1
            visited_coordinates.append(str(tail_position.x) + str(tail_position.y))


def move_up(moves):
    global head_position
    global tail_position
    global visited_coordinates
    for i in range(moves):
        head_position.y += 1
        if abs(tail_position.x - head_position.x) == 1 and abs(tail_position.y - head_position.y) == 2:
            tail_position.y += 1
            tail_position.x += 1 if tail_position.x - head_position.x == -1 else -1
            visited_coordinates.append(str(tail_position.x) + str(tail_position.y))
        if abs(tail_position.y - head_position.y) == 2:
            tail_position.y += 1
            visited_coordinates.append(str(tail_position.x) + str(tail_position.y))


def move_down(moves):
    global head_position
    global tail_position
    global visited_coordinates
    for i in range(moves):
        head_position.y -= 1
        if abs(tail_position.x - head_position.x) == 1 and abs(tail_position.y - head_position.y) == 2:
            tail_position.y -= 1
            tail_position.x += 1 if tail_position.x - head_position.x == -1 else -1
            visited_coordinates.append(str(tail_position.x) + str(tail_position.y))
        if abs(tail_position.y - head_position.y) == 2:
            tail_position.y -= 1
            visited_coordinates.append(str(tail_position.x) + str(tail_position.y))


if __name__ == '__main__':
    main()
