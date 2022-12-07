def main():
    file = open("input.txt")
    points_total_task1 = 0
    points_total_task2 = 0
    for line in file:
        values = line.strip().split(" ")
        points_total_task1 += calculate_points_task1(values)
        points_total_task2 += calculate_points_task2(values)
    file.close()
    print(points_total_task1)
    print(points_total_task2)


def calculate_points_task1(values):
    opponent = values[0]
    self = values[1]
    pick_points = {"X": 1, "Y": 2, "Z": 3}
    points = 0

    match opponent:
        case "A":
            match self:
                case "X":
                    points += 3
                case "Y":
                    points += 6
        case "B":
            match self:
                case "Y":
                    points += 3
                case "Z":
                    points += 6
        case "C":
            match self:
                case "X":
                    points += 6
                case "Z":
                    points += 3

    points += pick_points[self]

    return points


def calculate_points_task2(values):
    opponent = values[0]
    outcome = values[1]
    match_points = {"X": 0, "Y": 3, "Z": 6}
    points = 0
    points += match_points[outcome]

    match opponent:
        case "A":
            match outcome:
                case "X":
                    points += 3
                case "Y":
                    points += 1
                case "Z":
                    points += 2
        case "B":
            match outcome:
                case "X":
                    points += 1
                case "Y":
                    points += 2
                case "Z":
                    points += 3
        case "C":
            match outcome:
                case "X":
                    points += 2
                case "Y":
                    points += 3
                case "Z":
                    points += 1

    return points


if __name__ == '__main__':
    main()