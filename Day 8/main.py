from Util.file_reader import get_lines
import uuid


def main():
    file = open("test.txt")
    lines = get_lines(file)
    tree_matrix = []
    visibility_matrix = []
    for line in lines:
        tree_row = []
        visibility_row = []
        for x in line:
            tree_row.append(int(x))
            visibility_row.append(0)
        tree_matrix.append(tree_row)
        visibility_matrix.append(visibility_row)

    print(tree_matrix)
    print(visibility_matrix)
    mark_horizontal_trees(tree_matrix, visibility_matrix, True)
    print(visibility_matrix)


def mark_horizontal_trees(tree_matrix, visibility_matrix, reverse=False):
    x = 0
    while x < len(tree_matrix):
        y = 0
        row = tree_matrix[x][::-1] if reverse else tree_matrix[x]
        tree_row = []
        while y < len(row):
            if len(tree_row) == 0 or row[y] > max(tree_row):
                visibility_matrix[x][y] = 1
                tree_row.append(row[y])
            y += 1
        x += 1

    return visibility_matrix


if __name__ == '__main__':
    main()
