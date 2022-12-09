from Util.file_reader import get_lines
import uuid
from collections import Counter
import re


class Folder:
    def __init__(self, name, depth, guid, parent_guid=""):
        self.name = name
        self.parent_guid = parent_guid
        self.size = 0
        self.id = guid
        self.depth = depth


class File:
    def __init__(self, name, size, guid):
        self.name = name
        self.size = int(size)
        self.parent_guid = guid


def main():
    file = open("input.txt")
    lines = get_lines(file)
    current_depth = 0
    guid = uuid.uuid4()
    folder = Folder("/", current_depth, guid)
    folders = [folder]
    current_folder = guid
    files = []
    rounds = 0

    for line in lines:
        line_arr = line.split()
        if line_arr[0] == "dir":
            guid = uuid.uuid4()
            folder = Folder(line_arr[1], current_depth, guid, current_folder)
            folders.append(folder)

        if line_arr[0].isdigit():
            file = File(line_arr[1], line_arr[0], current_folder)
            files.append(file)
        if line_arr[0] == "$":
            if line_arr[1] == "cd":
                if line_arr[2] == "..":
                    for x in folders:
                        if x.id == current_folder:
                            current_folder = x.parent_guid
                            current_depth -= 1
                else:
                    for x in folders:
                        if x.name == line_arr[2] and x.parent_guid == current_folder:
                            current_folder = x.id
                            current_depth += 1
    for y in files:
        for x in folders:
            if y.parent_guid == x.id:
                x.size += y.size
                if x.parent_guid != "":
                    append_size(x.parent_guid, x.depth, y.size, folders)

    freeable_space = 0
    for x in folders:
        if x.size < 100000:
            freeable_space += x.size
    print("Task 1 answer: ", freeable_space)

    system_total = 70000000
    smallest_size = None
    current_taken_space = None
    smallest_directory = None
    for x in folders:
        if x.name == "/":
            current_taken_space = x.size
            continue
        minimum_space = system_total - (current_taken_space - x.size)
        if minimum_space > 30000000 and (minimum_space < current_taken_space or smallest_size is None):
            smallest_size = minimum_space
            smallest_directory = x.size
    print("Task 2 answer: ", smallest_directory)




def append_size(parent_guid, depth, size, folders):
    for x in folders:
        if x.id == parent_guid:
            x.size += size
            if (x.parent_guid != "") and (x.depth < depth):
                append_size(x.parent_guid, x.depth, size, folders)
    return


if __name__ == '__main__':
    main()
