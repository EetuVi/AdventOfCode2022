from Util.file_reader import get_lines
import uuid


def main():
    file = open("input.txt")
    lines = get_lines(file)
    tree_matrix = []
    visibility_matrix = []
    score_matrix = []
    for line in lines:
        tree_row = []
        visibility_row = []
        score_row = []
        for x in line:
            tree_row.append(int(x))
            visibility_row.append(0)
            score_row.append(0)
        tree_matrix.append(tree_row)
        visibility_matrix.append(visibility_row)
        score_matrix.append(score_row)

    mark_horizontal_trees(tree_matrix, visibility_matrix)
    mark_horizontal_trees(tree_matrix, visibility_matrix, True)
    mark_vertical_trees(tree_matrix, visibility_matrix)
    mark_vertical_trees(tree_matrix, visibility_matrix, True)
    total = 0
    for row in visibility_matrix:
        for num in row:
            if num == 1:
                total += 1

    print("Task 1 answer: ", total)

    x = 0
    while x < len(tree_matrix):
        y = 0
        while y < len(tree_matrix[0]):
            tree_score = calculate_scenic_score(tree_matrix, x, y)
            score_matrix[x][y] = tree_score
            y += 1
        x += 1

    highest = 0
    for row in score_matrix:
        for score in row:
            if highest < score:
                highest = score

    print("Task 2 answer: ", highest)


def mark_horizontal_trees(tree_matrix, visibility_matrix, reverse=False):
    x = 0
    while x < len(tree_matrix):
        y = 0
        row = tree_matrix[x][::-1] if reverse else tree_matrix[x]
        tree_row = []
        while y < len(row):
            if len(tree_row) == 0 or row[y] > max(tree_row):
                if reverse:
                    visibility_matrix[x][len(visibility_matrix[x]) - y - 1] = 1
                else:
                    visibility_matrix[x][y] = 1
                tree_row.append(row[y])
            y += 1
        x += 1

    return visibility_matrix


def mark_vertical_trees(tree_matrix, visibility_matrix, reverse=False):
    y = 0
    while y < len(tree_matrix[0]):
        x = 0
        col = []
        if reverse:
            reverse_matrix = tree_matrix[::-1]
            for row in reverse_matrix:
                col.append(row[y])
        else:
            for row in tree_matrix:
                col.append(row[y])
        tree_row = []
        while x < len(col):
            if len(tree_row) == 0 or col[x] > max(tree_row):
                if reverse:
                    visibility_matrix[len(visibility_matrix) - x - 1][y] = 1
                else:
                    visibility_matrix[x][y] = 1
                tree_row.append(col[x])
            x += 1
        y += 1

    return visibility_matrix


def calculate_scenic_score(tree_matrix, x, y):
    score_up = 0
    score_down = 0
    score_right = 0
    score_left = 0
    z = x - 1
    while z >= 0:
        if tree_matrix[z][y] < tree_matrix[x][y]:
            score_up += 1
        else:
            score_up += 1
            break
        z -= 1

    z = x + 1
    while z < len(tree_matrix[x]):
        if tree_matrix[z][y] < tree_matrix[x][y]:
            score_down += 1
        else:
            score_down += 1
            break
        z += 1

    z = y + 1
    while z < len(tree_matrix):
        if tree_matrix[x][z] < tree_matrix[x][y]:
            score_right += 1
        else:
            score_right += 1
            break
        z += 1

    z = y - 1
    while z >= 0:
        if tree_matrix[x][z] < tree_matrix[x][y]:
            score_left += 1
        else:
            score_left += 1
            break
        z -= 1

    return score_up * score_down * score_left * score_right


if __name__ == '__main__':
    main()
